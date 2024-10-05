import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from datetime import datetime
import os

# Definir directorios de salida
output_directory = './output/'
result_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)
os.makedirs(result_directory, exist_ok=True)

# 1. Procesar un CSV para la IA
def process_csv_for_ia(filename):
    """
    Procesa un CSV que contiene 'time_rel', 'time_abs' y 'velocity',
    para agregar 'delta_velocity', 'acceleration' y tiempo absoluto en formato numérico.
    """
    data_cat = pd.read_csv(filename)

    # Extraer las columnas de interés
    times_rel = np.array(data_cat['time_rel(sec)'].tolist())
    velocity = np.array(data_cat['velocity(m/s)'].tolist())

    # Calcular delta_velocity (diferencia de velocidades consecutivas)
    delta_velocity = np.diff(velocity, prepend=velocity[0])

    # Calcular la aceleración (cambio de velocidad en función del tiempo)
    delta_time = np.diff(times_rel, prepend=times_rel[0])
    delta_time[delta_time == 0] = np.nan  # Para evitar dividir por 0
    acceleration = delta_velocity / delta_time

    # Convertir el tiempo absoluto a formato numérico (segundos desde el epoch)
    time_abs_numeric = pd.to_datetime(data_cat['time_abs(%Y-%m-%dT%H:%M:%S.%f)']).astype('int64') / 10**9

    # Crear DataFrame con todas las columnas necesarias para la IA
    processed_df = pd.DataFrame({
        'time_rel(sec)': times_rel,
        'velocity(m/s)': velocity,
        'delta_velocity(m/s^2)': delta_velocity,
        'acceleration(m/s^2)': acceleration,
        'time_abs_numeric': time_abs_numeric
    })

    # Eliminar filas con NaN
    processed_df = processed_df.dropna()

    # Escalar los datos para el modelo
    scaler = StandardScaler()
    processed_df[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)', 'time_abs_numeric']] = \
        scaler.fit_transform(processed_df[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)', 'time_abs_numeric']])

    return processed_df

# 2. Función para limpiar y preparar los datos de entrenamiento
def clean_data(data_file):
    """
    Limpia los datos, asegurando que la columna 'is_sismo_start' solo tenga valores binarios.
    También convierte el tiempo absoluto a una representación numérica.
    """
    data = pd.read_csv(data_file, low_memory=False)

    # Convertir el tiempo absoluto a formato numérico (segundos desde el epoch)
    data['time_abs_numeric'] = pd.to_datetime(data['time_abs(%Y-%m-%dT%H:%M:%S.%f)']).astype('int64') / 10**9

    # Convertir valores no numéricos a NaN y luego eliminar filas con NaN
    data['is_sismo_start'] = pd.to_numeric(data['is_sismo_start'], errors='coerce')
    data = data.dropna(subset=['is_sismo_start'])

    # Asegurarse de que los valores de 'is_sismo_start' sean solo 0 o 1
    data['is_sismo_start'] = data['is_sismo_start'].astype(int)
    data['is_sismo_start'] = data['is_sismo_start'].replace({1: True, 0: False})

    return data

# 3. Entrenar el modelo de IA usando RandomForestClassifier
def train_randomforest_model(data_file):
    """
    Entrena un modelo RandomForest utilizando los datos CSV limpios.
    """
    # Limpiar los datos antes de usarlos
    data = clean_data(data_file)

    # Incluir el tiempo absoluto numérico en las características
    X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])
    y = data['is_sismo_start']

    # Escalar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Entrenar el modelo RandomForest con ajuste de peso en las clases
    model = RandomForestClassifier(class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print(classification_report(y_test, y_pred))

    # Guardar el modelo
    model_path = f'{output_directory}randomforest_sismo_detection_model.pkl'
    pd.to_pickle(model, model_path)
    print("Modelo guardado correctamente.")

    return model

# 4. Predecir con el modelo ya entrenado
def detect_sismo(model, processed_data, inicio_sismo_epoch, threshold=0.2):
    """
    Usa un modelo de IA entrenado para predecir si hay sismo o no en un nuevo CSV.
    Ajusta el umbral para generar más valores True.
    """
    # Usamos el DataFrame procesado previamente
    X_new = processed_data[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)', 'time_abs_numeric']]

    # Obtener probabilidades en lugar de predicciones directas
    probabilities = model.predict_proba(X_new)[:, 1]

    # Aplicar el umbral personalizado y convertirlo a Series de pandas para usar replace
    predictions = pd.Series((probabilities > threshold).astype(int))

    # Convertir predicciones de 0/1 a False/True
    predictions = predictions.replace({1: True, 0: False})

    # Agregar las predicciones al DataFrame original
    processed_data['is_sismo_predicted'] = predictions

    # Filtrar solo las filas que tengan predicción True
    true_predictions = processed_data[processed_data['is_sismo_predicted'] == True]

    # Limitar a 10 predicciones y seleccionar una aleatoria
    true_predictions = true_predictions.head(10)
    if not true_predictions.empty:
        random_prediction = true_predictions.sample(1)
    else:
        print("No se encontraron predicciones con valor True.")
        return None

    # Obtener la fecha legible basándose en el tiempo absoluto inicial (inicio_sismo_epoch)
    random_prediction['time_abs_human_readable'] = random_prediction['time_rel(sec)'].apply(
        lambda x: datetime.utcfromtimestamp(inicio_sismo_epoch + x).strftime('%Y-%m-%d %H:%M:%S.%f UTC')
    )

    # Mostrar resultados
    print("Predicción seleccionada:")
    print(random_prediction[['time_rel(sec)', 'is_sismo_predicted', 'time_abs_human_readable']])

    # Guardar el resultado en formato JSON
    output_file = f'{result_directory}random_prediction.json'
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Archivo existente {output_file} eliminado.")

    random_prediction.to_json(output_file, orient='records', lines=True)
    print(f"Predicción guardada en {output_file}")

    return random_prediction.to_json(orient='records', lines=True)

def predict_sismo():
    return detect_sismo(model, processed_data, inicio_sismo_epoch=inicio_sismo_epoch, threshold=0.2)

# Procesar y entrenar el modelo
csv_test_file = './data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1975-06-26HR00_evid00198.csv'
processed_data = process_csv_for_ia(csv_test_file)

# Entrenar el modelo
model = train_randomforest_model('./output/detection_catalog_scaled.csv')

# Predecir usando el modelo entrenado
# Establecer inicio_sismo_epoch al 5 de octubre de 2024
inicio_sismo_epoch = 1759622400

# Predecir sismos
# predict_sismo()
