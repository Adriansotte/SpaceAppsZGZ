import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

# Directorios de salida
output_directory = './output/'
result_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)

# 1. Procesar un CSV para la IA (archivo de testeo)
def process_csv_for_ia(filename):
    """
    Procesa un CSV que contiene 'time_rel', 'time_abs' y 'velocity',
    para agregar 'delta_velocity' y 'acceleration' que la IA puede usar.
    También extrae el primer valor absoluto de tiempo como el inicio del sismo.
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

    # Obtener el primer valor absoluto del tiempo (inicio del sismo)
    first_time_abs = data_cat['time_abs(%Y-%m-%dT%H:%M:%S.%f)'].iloc[0]

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
        scaler.fit_transform(
            processed_df[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']])

    return processed_df, first_time_abs


# 2. Predecir con el modelo ya entrenado
def detect_sismo(model, processed_data, first_time_abs, threshold=0.3):
    """
    Usa un modelo de IA entrenado para predecir si hay sismo o no en un nuevo CSV de testeo.
    Ajusta el umbral para generar más valores True. Retorna un solo True si lo hay,
    o un solo False si no hay ningún True. Además, añade el primer tiempo absoluto al JSON.
    """
    # Usamos el DataFrame procesado previamente
    X_new = processed_data[['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']]

    # Obtener probabilidades en lugar de predicciones directas
    probabilities = model.predict_proba(X_new)[:, 1]

    # Aplicar el umbral personalizado
    predictions = probabilities > threshold

    # Agregar las predicciones al DataFrame original
    processed_data['is_sismo_predicted'] = predictions

    # Filtrar las filas que tienen True
    true_predictions = processed_data[processed_data['is_sismo_predicted'] == True]

    # Si hay predicciones True, devolver la primera; si no, devolver una fila con False
    if not true_predictions.empty:
        result = true_predictions.iloc[0:1]  # Devolver solo la primera fila con True
    else:
        result = processed_data.iloc[0:1].copy()  # Tomar una fila cualquiera
        result['is_sismo_predicted'] = False  # Forzar a False si no hay True

    # Añadir el primer valor absoluto de tiempo al DataFrame resultante
    result['first_time_abs'] = first_time_abs

    # Guardar el resultado en formato JSON
    output_file = f'{result_directory}predictions.json'
    result.to_json(output_file, orient='records', lines=True)
    print(f"Predicción guardada en {output_file}")

    # Retornar el resultado en formato JSON
    return result.to_json(orient='records', lines=True)


# Función para identificar si hay sismo en un nuevo CSV
def identificarSismoONoSismo(csv_file):
    processed_data, first_time_abs = process_csv_for_ia(csv_file)
    return detect_sismo(model, processed_data, first_time_abs, threshold=0.3)


# 3. Entrenar el modelo (o cargar uno entrenado)
def entrenar_modelo(data_file):
    """
    Entrena el modelo RandomForest utilizando los datos del archivo CSV de entrenamiento.
    """
    data = pd.read_csv(data_file)

    # Dividir los datos
    X = data.drop(columns=['is_sismo_start', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)'])
    y = data['is_sismo_start']

    # Escalar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Entrenar el modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42,
                                   class_weight='balanced')  # Aumentar peso de los sismos
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    model.fit(X_train, y_train)

    print(f"Modelo entrenado con precisión: {model.score(X_test, y_test)}")

    # Guardar el modelo entrenado
    model_path = f'{output_directory}random_forest_sismo_model.pkl'
    pd.to_pickle(model, model_path)
    print(f"Modelo guardado en {model_path}")

    return model


# Entrenar el modelo (si no hay uno guardado ya)
data_file = './output/detection_catalog_scaled_mars.csv'
model = entrenar_modelo(data_file)

# Ejemplo de predicción con un archivo CSV de testeo
csv_file = './data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1975-06-26HR00_evid00198.csv'
identificarSismoONoSismo(csv_file)