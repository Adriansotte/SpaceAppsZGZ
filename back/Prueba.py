# Importar bibliotecas
import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

# Directorio del catálogo y archivo del catálogo
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'

# Leer el archivo del catálogo
cat = pd.read_csv(cat_file)
print(cat.head())

# Seleccionar una detección (primer evento sísmico en este caso)
row = cat.iloc[0]

# Obtener el tiempo de llegada absoluto
arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f')
print(f'Absolute Arrival Time: {arrival_time}')

# Obtener el tiempo relativo
arrival_time_rel = row['time_rel(sec)']
print(f'Relative Arrival Time: {arrival_time_rel}')

# Obtener el nombre del archivo correspondiente al evento sísmico
test_filename = row['filename']
print(f'File Name: {test_filename}')

# Leer el archivo CSV correspondiente al evento
data_directory = './data/lunar/training/data/S12_GradeA/'
csv_file = f'{data_directory}{test_filename}.csv'

# Leer los datos del archivo CSV
data_cat = pd.read_csv(csv_file)
print(data_cat.head())

# Extraer los tiempos y velocidades para trazar el gráfico
csv_times = np.array(data_cat['time_rel(sec)'].tolist())
csv_data = np.array(data_cat['velocity(m/s)'].tolist())

# Graficar los datos del evento
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.plot(csv_times, csv_data)

# Personalizar el gráfico
ax.set_xlim([min(csv_times), max(csv_times)])
ax.set_ylabel('Velocity (m/s)')
ax.set_xlabel('Time (s)')
ax.set_title(f'{test_filename}', fontweight='bold')

# Marcar la llegada del evento
arrival_line = ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
ax.legend(handles=[arrival_line])

plt.show()
