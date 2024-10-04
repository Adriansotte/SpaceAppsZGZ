import os

import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime, timedelta


def extract_data(filename, data_directory):
    """
    Dependiendo de la extensión del archivo, se extraen los datos
    de un archivo CSV o MiniSEED y se retornan.
    """
    extension = os.path.splitext(filename)[-1][1:]

    if extension == 'csv':
        return extract_from_csv(filename, data_directory)
    elif extension == 'mseed':
        return extract_from_mseed(filename, data_directory)
    else:
        raise ValueError(
            "Formato de archivo no soportado. Solo se admiten CSV y MiniSEED. Valor actual: " + extension)


def extract_from_csv(filename, data_directory):
    """
    Extrae los datos de un archivo CSV y los retorna.
    """
    csv_file = f'{data_directory}{filename}'
    data_cat = pd.read_csv(csv_file)

    times_rel = np.array(data_cat['time_rel(sec)'].tolist())  # Tiempo relativo
    times_abs = np.array(data_cat['time_abs(%Y-%m-%dT%H:%M:%S.%f)'].tolist())  # Tiempo absoluto
    data = np.array(data_cat['velocity(m/s)'].tolist())  # Datos de velocidad
    start_time = times_abs[0]  # El primer valor del tiempo absoluto es el inicio del registro

    print(times_rel, times_abs, data, start_time)
    return times_rel, times_abs, data, start_time


def extract_from_mseed(filename, data_directory):
    """
    Extrae los datos de un archivo MiniSEED y los retorna.
    """
    mseed_file = f'{data_directory}{filename}'
    st = read(mseed_file)
    tr = st.traces[0].copy()

    times_rel = tr.times()  # Tiempo en segundos desde el inicio
    data = tr.data  # Datos de velocidad
    start_time = tr.stats.starttime.datetime  # Tiempo de inicio del registro

    # Calcula tiempos absolutos a partir del tiempo relativo y el tiempo de inicio
    times_abs = np.array([start_time + timedelta(seconds=t) for t in times_rel])

    print(times_rel, times_abs, data, start_time)
    return times_rel, times_abs, data, start_time

