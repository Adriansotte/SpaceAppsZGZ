import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os
from scipy import signal
from obspy.signal.trigger import classic_sta_lta
from matplotlib import cm


# Función para extraer datos desde un archivo CSV
def extract_data_from_csv(csv_file):
    """
    Función para extraer datos de un archivo CSV, retornando tiempos relativos, tiempos absolutos y datos de velocidad.
    :param csv_file: Ruta del archivo CSV
    :return: (times_rel, times_abs, csv_data) - tiempos relativos, tiempos absolutos, datos de velocidad
    """
    # Leer el archivo CSV
    data_cat = pd.read_csv(csv_file)

    # Extraer tiempos relativos y datos de velocidad
    csv_times = np.array(data_cat['time_rel(sec)'].tolist())
    csv_data = np.array(data_cat['velocity(m/s)'].tolist())

    # Convertir tiempo absoluto de cadena a formato datetime
    csv_times_dt = [datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f') for val in
                    data_cat['time_abs(%Y-%m-%dT%H:%M:%S.%f)'].values]

    return csv_times, csv_times_dt, csv_data


# Procesar los datos de un archivo CSV específico y generar gráficos
def process_seismic_data_from_csv(csv_file):
    """
    Procesa datos sísmicos desde un archivo CSV y genera gráficos.
    :param csv_file: Ruta al archivo CSV
    :return: Ruta relativa donde se guardaron las imágenes
    """
    # Extraer los datos del archivo CSV
    csv_times, csv_times_dt, csv_data = extract_data_from_csv(csv_file)

    # Obtener el nombre base del archivo CSV (sin la extensión)
    base_name = os.path.splitext(os.path.basename(csv_file))[0]

    # Ruta base de salida para las imágenes (ruta absoluta)
    base_output_directory = os.path.abspath(
        '../front/seismic/src/assets/'
    )

    # Crear un directorio con el nombre del archivo CSV dentro de la ruta de salida
    output_directory = os.path.join(base_output_directory, base_name)
    os.makedirs(output_directory, exist_ok=True)  # Asegúrate de que el directorio exista

    # Normalizar la ruta para que los separadores sean consistentes
    output_directory = os.path.normpath(output_directory)

    # Graficar la traza sísmica relativa
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times, csv_data)
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')
    ax.set_title(f'{os.path.basename(csv_file)} - Seismic Trace Relative')

    # Guardar la imagen de la traza sísmica relativa
    plt.savefig(os.path.join(output_directory, f'{base_name}_seismic_trace_rel.png'))
    plt.close()  # Cerrar la figura para evitar duplicados

    # Graficar la traza sísmica absoluta
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times_dt, csv_data)
    ax.set_xlim((min(csv_times_dt), max(csv_times_dt)))
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (month-day hour)')
    ax.set_title(f'{os.path.basename(csv_file)} - Seismic Trace Absolute')

    # Guardar la imagen de la traza sísmica absoluta
    plt.savefig(os.path.join(output_directory, f'{base_name}_seismic_trace_abs.png'))
    plt.close()  # Cerrar la figura para evitar duplicados

    # Aplicar filtro de paso de banda (opcional)
    filtered_data = csv_data  # Simulación de filtro, puedes aplicar uno real aquí

    # Espectrograma
    f, t, sxx = signal.spectrogram(filtered_data, fs=1.0 / (csv_times[1] - csv_times[0]))
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    ax1.plot(csv_times, filtered_data)
    ax1.set_xlim([min(csv_times), max(csv_times)])
    ax1.set_ylabel('Velocity (m/s)')
    ax1.set_xlabel('Time (s)')
    ax2.pcolormesh(t, f, sxx, cmap=cm.jet, shading='auto')
    ax2.set_xlim([min(csv_times), max(csv_times)])
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Frequency (Hz)')
    plt.colorbar(ax2.pcolormesh(t, f, sxx, cmap=cm.jet), ax=ax2, orientation='horizontal').set_label(
        'Power ((m/s)^2/sqrt(Hz))')

    # Guardar la imagen del espectrograma
    plt.savefig(os.path.join(output_directory, f'{base_name}_spectrogram.png'))
    plt.close()  # Cerrar la figura para evitar duplicados

    # Calcular STA/LTA
    sta_len = 30
    lta_len = 150
    cft = classic_sta_lta(csv_data, int(sta_len * (1 / (csv_times[1] - csv_times[0]))),
                          int(lta_len * (1 / (csv_times[1] - csv_times[0]))))

    # Normalizar la función característica
    cft = cft / np.max(cft)
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times, cft)
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylim([0, 10])
    ax.set_ylabel('Characteristic Function')
    ax.set_xlabel('Time (s)')
    plt.savefig(os.path.join(output_directory, f'{base_name}_sta_lta.png'))
    plt.close()  # Cerrar la figura para evitar duplicados

    print(f"Procesamiento completo para {os.path.basename(csv_file)}.")

    # Devolver la ruta relativa donde se guardaron las imágenes
    relative_output_directory = os.path.relpath(output_directory)
    return relative_output_directory
