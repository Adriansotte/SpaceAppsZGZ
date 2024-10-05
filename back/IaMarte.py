import numpy as np
import pandas as pd
from imblearn.over_sampling import ADASYN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

# Directorio de salida
output_directory = './back/output/'
result_directory = './back/Resultados/'
os.makedirs(output_directory, exist_ok=True)

# 1. Procesar un CSV para la IA (archivo de testeo)
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
    delta_time[delta_time == 0] = np.nan  # Para evitar dividir por 0
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

# 2. Predecir con el modelo ya entrenado
def detect_sismo(model, processed_data, threshold=0.3):
    """
    Usa un modelo de IA entrenado para predecir si hay sismo o no en un nuevo CSV de testeo.
    Ajusta el umbral para generar más valores `True`.
    """
    # Usamos el DataFrame procesado previamente
    X_new = processed_data[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']]

    # Obtener probabilidades en lugar de predicciones directas
    probabilities = model.predict_proba(X_new)[:, 1]

    # Aplicar el umbral personalizado
    predictions = probabilities > threshold

    # Agregar las predicciones al DataFrame original
    processed_data['is_sismo_predicted'] = predictions

    # Mostrar resultados y guardar en CSV
    print("Predicciones completadas:")
    print(processed_data[['time_rel(sec)', 'is_sismo_predicted']])

    output_file = f'{result_directory}predictions.csv'
    processed_data.to_csv(output_file, index=False)
    print(f"Predicciones guardadas en {result_directory}")

# Ejemplo de uso con un arcdhivo CSV de testeo
csv_file = f'./back/data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1975-06-26HR00_evid00198.csv'

# 1. Procesar el CSV de testeo para la IA
processed_data = process_csv_for_ia(csv_file)

# 2. Entrenar el modelo (o cargar uno entrenado)
data_file = './output/detection_catalog_scaled_mars.csv'
data = pd.read_csv(data_file)
X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])
y = data['is_sismo_start']

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')  # Aumentar peso de los sismos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)

# 3. Predecir si hay sismo en el nuevo archivo de testeo con umbral ajustado
detect_sismo(model, processed_data, threshold=0.3)
