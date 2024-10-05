import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os
from obspy.signal.trigger import classic_sta_lta, trigger_onset
from sklearn.preprocessing import StandardScaler
from joblib import Parallel, delayed

# Directorio de salida para el CSV
output_directory = './output/'
os.makedirs(output_directory, exist_ok=True)  # Asegúrate de que el directorio exista

# Cargar los datos del catálogo de Marte
cat_directory = './data/mars/training/catalogs/'
cat_file = cat_directory + 'Mars_InSight_training_catalog_final.csv'
cat = pd.read_csv(cat_file)

# Crear el DataFrame de salida sin la columna 'filename'
output_df = pd.DataFrame(columns=[
    'time_rel(sec)', 'time_abs(%Y-%m-%dT%H:%M:%S.%f)', 'velocity(m/s)', 'delta_velocity(m/s^2)',
    'acceleration(m/s^2)', 'is_sismo_start'
])

# Parámetros STA/LTA
sta_len = 30
lta_len = 150
thr_on = 4
thr_off = 1.5

# Función que procesa cada archivo
def process_file(row, file_index):
    try:
        # Verificar si la columna filename existe y si el valor no es NaN
        if pd.isna(row['filename']):
            print("Filename is missing, skipping this row...")
            return pd.DataFrame()

        # Obtener el tiempo de llegada absoluto y relativo
        arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f')
        test_filename = row['filename']
        print(f"Processing file: {test_filename}")

        # Leer los datos del archivo CSV correspondiente
        data_directory = './data/mars/training/data/'
        csv_file = f'{data_directory}{test_filename}'

        # Comprobar si el archivo existe antes de continuar
        if not os.path.exists(csv_file):
            print(f"File {csv_file} not found, skipping...")
            return pd.DataFrame()

        data_cat = pd.read_csv(csv_file)

        # Extraer los datos de tiempo relativo y velocidad
        csv_times = np.array(data_cat['time_rel(sec)'].tolist())
        csv_data = np.array(data_cat['velocity(c/s)'].tolist())

        # Convertir solo los dos primeros archivos de c/s a m/s
        if file_index < 2:
            csv_data = csv_data / 100  # Convertir de c/s a m/s solo para los primeros archivos
            print(f"Converted velocity from c/s to m/s for {test_filename}")

        # Verificar si los datos son suficientes para el cálculo STA/LTA
        if len(csv_data) >= lta_len:
            # Calcular la característica STA/LTA
            cft = classic_sta_lta(csv_data, int(sta_len * (1 / (csv_times[1] - csv_times[0]))),
                                  int(lta_len * (1 / (csv_times[1] - csv_times[0]))))

            # Aplicar el umbral para detectar el inicio del sismo
            on_off = np.array(trigger_onset(cft, thr_on, thr_off))

            # Si no se encuentra ningún evento, pasar al siguiente archivo
            if len(on_off) == 0:
                print(f"No triggers found for {test_filename}")
                return pd.DataFrame()  # Retornar un DataFrame vacío si no hay eventos

            # Calcular la delta de la velocidad (cambio de velocidad entre tiempos consecutivos)
            delta_velocity = np.diff(csv_data, prepend=csv_data[0])

            # Calcular la aceleración (cambio de la velocidad respecto al tiempo)
            delta_time = np.diff(csv_times, prepend=csv_times[0])
            delta_time[delta_time == 0] = np.nan  # Reemplazar los ceros por NaN para evitar errores de división
            acceleration = delta_velocity / delta_time

            # Iterar a través de los triggers detectados
            for trigger in on_off:
                # Registrar el tiempo de inicio del sismo
                sismo_start_time_rel = csv_times[trigger[0]]  # Tiempo relativo del inicio del sismo
                sismo_start_time_abs = arrival_time + timedelta(seconds=sismo_start_time_rel)  # Tiempo absoluto

                # Crear un DataFrame temporal con la información de cada fila
                temp_df = pd.DataFrame({
                    'time_rel(sec)': csv_times,
                    'time_abs(%Y-%m-%dT%H:%M:%S.%f)': [
                        datetime.strftime(arrival_time + timedelta(seconds=t), '%Y-%m-%dT%H:%M:%S.%f') for t in csv_times],
                    'velocity(m/s)': csv_data,
                    'delta_velocity(m/s^2)': delta_velocity,
                    'acceleration(m/s^2)': acceleration,
                    'is_sismo_start': [i == trigger[0] for i in range(len(csv_times))]
                })

                return temp_df

    except FileNotFoundError:
        # Manejar el caso en que el archivo CSV no exista
        print(f"File {test_filename} not found. Skipping...")
        return pd.DataFrame()  # Retornar un DataFrame vacío en caso de error

    except Exception as e:
        # Capturar cualquier otro error inesperado
        print(f"An error occurred while processing {test_filename}: {e}")
        return pd.DataFrame()  # Retornar un DataFrame vacío en caso de error

# Procesar los archivos en paralelo usando joblib
num_jobs = -1  # Usar todos los núcleos disponibles
results = Parallel(n_jobs=num_jobs)(delayed(process_file)(row, index) for index, row in cat.iterrows())

# Concatenar los resultados procesados
output_df = pd.concat(results, ignore_index=True)

# Escalar las características numéricas antes de guardar el CSV
if not output_df.empty:
    scaler = StandardScaler()
    columns_to_scale = ['time_rel(sec)', 'velocity(m/s)', 'delta_velocity(m/s^2)', 'acceleration(m/s^2)']
    output_df[columns_to_scale] = scaler.fit_transform(output_df[columns_to_scale])

    # Guardar el archivo CSV de salida con datos escalados
    output_df.to_csv(f'{output_directory}detection_catalog_scaled_mars.csv', index=False)
    print("CSV escalado y generado correctamente.")
else:
    print("No data processed. No CSV generated.")