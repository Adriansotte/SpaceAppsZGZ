import numpy as np
import pandas as pd
from imblearn.over_sampling import ADASYN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import os

# Definir directorios de salida
output_directory = './output/'
result_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)
os.makedirs(result_directory, exist_ok=True)

# Función para procesar el CSV y preparar los datos para la IA
def process_csv_for_ia(filename):
    """
    Procesa un CSV que contiene 'time_rel', 'time_abs' y 'velocity',
    para agregar 'delta_velocity' y 'acceleration' que la IA puede usar.
    """
    data_cat = pd.read_csv(filename)

    # Extraer las columnas de interés
    times_rel = np.array(data_cat['time_rel(sec)'].tolist())
    velocity = np.array(data_cat['velocity(m/s)'].tolist())

    # Calcular delta_velocity (diferencia de velocidades consecutivas)
    delta_velocity = np.diff(velocity, prepend=velocity[0])

    # Calcular la aceleración (cambio de velocidad en función del tiempo)
    delta_time = np.diff(times_rel, prepend=times_rel[0])
    delta_time[delta_time == 0] = np.nan  # Evitar divisiones por 0
    acceleration = delta_velocity / delta_time

    # Crear DataFrame con todas las columnas necesarias para la IA
    processed_df = pd.DataFrame({
        'time_rel(sec)': times_rel,
        'velocity(m/s)': velocity,
        'delta_velocity(m/s^2)': delta_velocity,
        'acceleration(m/s^2)': acceleration,
    })

    # Eliminar filas con NaN
    processed_df = processed_df.dropna()

    # Escalar los datos para el modelo
    scaler = StandardScaler()
    processed_df[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']] = \
        scaler.fit_transform(processed_df[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']])

    return processed_df

# Función para crear el modelo de red neuronal
def create_model(input_dim):
    """
    Define el modelo secuencial para la IA.
    """
    model = Sequential()
    model.add(Dense(128, activation='relu', input_dim=input_dim))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Activación sigmoide para clasificación binaria
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Función para entrenar el modelo de IA
def train_model(data_file):
    """
    Entrena el modelo de IA utilizando los datos CSV escalados y ADASYN para balancear la clase minoritaria.
    """
    # Cargar el archivo CSV con los datos escalados
    data = pd.read_csv(data_file)

    # Eliminar la columna 'time_abs' ya que es un valor de fecha
    X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])
    y = data['is_sismo_start']

    # Imputar valores faltantes (NaN) con la media
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    # Escalar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    # Balancear los datos con ADASYN
    adasyn = ADASYN(random_state=42)
    X_resampled, y_resampled = adasyn.fit_resample(X_scaled, y)

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

    # Crear el modelo
    model = create_model(X_train.shape[1])

    # Early stopping para evitar sobreajuste
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    # Entrenamiento del modelo
    model.fit(X_train, y_train, validation_split=0.2, epochs=100, batch_size=32, callbacks=[early_stopping])

    # Evaluar el modelo en el conjunto de prueba
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Loss: {loss}, Accuracy: {accuracy}')

    # Guardar el modelo
    model.save(f'{output_directory}sismo_detection_model.h5')
    print("Modelo guardado correctamente.")

    return model

# Función para predecir sismos con el modelo ya entrenado
def detect_sismo_with_tf(model, processed_data, threshold=0.5):
    """
    Usa un modelo de IA entrenado para predecir si hay sismo o no en un nuevo CSV.
    Ajusta el umbral para generar más valores `True`.
    """
    # Usamos el DataFrame procesado previamente
    X_new = processed_data[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']]

    # Obtener probabilidades en lugar de predicciones directas
    probabilities = model.predict(X_new)

    # Aplicar el umbral personalizado
    predictions = (probabilities > threshold).astype(int)

    # Agregar las predicciones al DataFrame original
    processed_data['is_sismo_predicted'] = predictions

    # Mostrar resultados y guardar en CSV
    print("Predicciones completadas:")
    print(processed_data[['time_rel(sec)', 'is_sismo_predicted']])

    output_file = f'{result_directory}predictions.csv'
    processed_data.to_csv(output_file, index=False)
    print(f"Predicciones guardadas en {output_file}")

# Ejecutar todo el proceso
csv_test_file = './data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1975-06-26HR00_evid00198.csv'
processed_data = process_csv_for_ia(csv_test_file)

# Entrenar el modelo con el archivo de datos escalados
model = train_model('./output/detection_catalog_scaled.csv')

# Predecir usando el modelo entrenado
detect_sismo_with_tf(model, processed_data, threshold=0.3)
