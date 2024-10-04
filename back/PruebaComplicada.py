import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from obspy.signal.trigger import classic_sta_lta, trigger_onset
from matplotlib import cm
from datetime import timedelta

# Directorio de salida para las imágenes
output_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)  # Asegúrate de que el directorio exista


def process_and_generate_plots_from_extractor(times_rel, times_abs, data, start_time):
    """
    Procesa los datos sísmicos recibidos y genera imágenes de traza sísmica, función característica,
    espectrograma y detecciones, guardándolos en un directorio especificado.

    Parameters:
    times_rel (array): Tiempos relativos extraídos.
    times_abs (array): Tiempos absolutos extraídos.
    data (array): Datos de velocidad (m/s).
    start_time (datetime): Tiempo absoluto de inicio del sismo.

    Returns:
    str: Directorio donde se guardan las imágenes generadas.
    """

    csv_file = "output_data"  # Puedes ajustar este nombre según sea necesario

    # Asegurarse de que arrival_time_rel está dentro de los límites de times_rel
    arrival_time_rel = times_rel[0]  # O ajustar el valor adecuado para la llegada del sismo
    if not (min(times_rel) <= arrival_time_rel <= max(times_rel)):
        print(f"arrival_time_rel ({arrival_time_rel}) fuera del rango de times_rel.")
        arrival_time_rel = np.median(times_rel)  # Definir a un valor dentro del rango como solución temporal

    # Plot de la traza sísmica relativa y guarda imagen
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(times_rel, data)
    ax.set_xlim([min(times_rel), max(times_rel)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')
    ax.set_title(f'{csv_file}', fontweight='bold')

    # Dibujar la línea roja en arrival_time_rel si está dentro del rango
    ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
    ax.legend()

    plt.savefig(f'{output_directory}{csv_file}_seismic_trace_rel.png')

    # Plot de la traza en tiempo absoluto y guarda imagen
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(times_abs, data)
    ax.set_xlim([min(times_abs), max(times_abs)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (month-day hour)')
    ax.set_title(f'{csv_file}', fontweight='bold')

    if start_time >= min(times_abs) and start_time <= max(times_abs):
        ax.axvline(x=start_time, c='red', label='Abs. Arrival')
        ax.legend()

    plt.savefig(f'{output_directory}{csv_file}_seismic_trace_abs.png')

    # Aplicar un filtro de paso de banda (simulado)
    filtered_data = data  # Línea de filtro dummy, podrías aplicar un filtro real aquí

    # Generar un espectrograma y guardar imagen
    f, t, sxx = signal.spectrogram(filtered_data, fs=1.0 / (times_rel[1] - times_rel[0]))
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Serie temporal
    ax1.plot(times_rel, filtered_data)
    ax1.axvline(x=arrival_time_rel, color='red', label='Detection')
    ax1.set_xlim([min(times_rel), max(times_rel)])
    ax1.set_ylabel('Velocity (m/s)')
    ax1.set_xlabel('Time (s)')
    ax1.legend()

    # Espectrograma
    vals = ax2.pcolormesh(t, f, sxx, cmap=cm.jet, vmax=5e-17)
    ax2.set_xlim([min(times_rel), max(times_rel)])
    ax2.set_xlabel('Time (Day Hour:Minute)', fontweight='bold')
    ax2.set_ylabel('Frequency (Hz)', fontweight='bold')
    ax2.axvline(x=arrival_time_rel, c='red')
    plt.colorbar(vals, ax=ax2, orientation='horizontal').set_label('Power ((m/s)^2/sqrt(Hz))', fontweight='bold')

    plt.savefig(f'{output_directory}{csv_file}_spectrogram.png')

    # Calcular STA/LTA y guardar la función característica
    sta_len = 30
    lta_len = 150
    cft = classic_sta_lta(data, int(sta_len * (1 / (times_rel[1] - times_rel[0]))),
                          int(lta_len * (1 / (times_rel[1] - times_rel[0]))))
    cft /= np.max(cft)  # Normaliza la función característica
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    ax.plot(times_rel, cft)
    ax.set_xlim([min(times_rel), max(times_rel)])
    ax.set_ylim([0, 10])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Characteristic function')
    plt.savefig(f'{output_directory}{csv_file}_characteristic_function.png')

    # Aplicar umbral de detección
    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))

    if len(on_off) == 0:
        print(f"No triggers found for {csv_file}")
        return output_directory

    # Plotear las detecciones y guardar la imagen
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    for i, triggers in enumerate(on_off):
        ax.axvline(x=times_rel[triggers[0]], color='red', label=f'Trig. On {i + 1}')
        ax.axvline(x=times_rel[triggers[1]], color='purple', label=f'Trig. Off {i + 1}')
    ax.plot(times_rel, data)
    ax.set_xlim([min(times_rel), max(times_rel)])
    ax.legend()
    plt.savefig(f'{output_directory}{csv_file}_triggers.png')

    # Generar catálogo de detecciones y guardarlo en CSV
    detection_times = []
    for i, triggers in enumerate(on_off):
        on_time = times_rel[triggers[0]] + arrival_time_rel
        detection_times.append((start_time + timedelta(seconds=on_time)).strftime('%Y-%m-%dT%H:%M:%S.%f'))

    detect_df = pd.DataFrame({'filename': csv_file,
                              'time_abs(%Y-%m-%dT%H:%M:%S.%f)': detection_times,
                              'time_rel(sec)': times_rel[on_off[:, 0]]})
    detect_df.to_csv(f'{output_directory}detection_catalog_{csv_file}.csv', index=False)

    return output_directory
