import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

from scipy import signal
from obspy.signal.trigger import classic_sta_lta, trigger_onset
from matplotlib import cm

# Directorio de salida para las imágenes
output_directory = './Resultados/'
os.makedirs(output_directory, exist_ok=True)  # Asegúrate de que el directorio exista

# %% Load the catalog data
cat_directory = './data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
cat.head()

# %% Select a detection from the catalog
for index, row in cat.iterrows():
    arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], '%Y-%m-%dT%H:%M:%S.%f')
    print(f"Arrival Time: {arrival_time}")

    # Get the relative arrival time and filename
    arrival_time_rel = row['time_rel(sec)']
    test_filename = row.filename
    print(f"Processing file: {test_filename}")

    # Read the corresponding CSV data
    data_directory = './data/lunar/training/data/S12_GradeA/'
    csv_file = f'{data_directory}{test_filename}.csv'
    data_cat = pd.read_csv(csv_file)

    # Extract time and velocity data
    csv_times = np.array(data_cat['time_rel(sec)'].tolist())
    csv_data = np.array(data_cat['velocity(m/s)'].tolist())

    # Plot the seismic trace and save image
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times, csv_data)

    # Customize the plot
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')
    ax.set_title(f'{test_filename}', fontweight='bold')

    # Plot the arrival time
    arrival_line = ax.axvline(x=arrival_time_rel, c='red', label='Rel. Arrival')
    ax.legend(handles=[arrival_line])

    # Save the plot as image
    plt.savefig(f'{output_directory}{test_filename}_seismic_trace_rel.png')


    # Convert time to absolute and plot
    csv_times_dt = [datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f') for val in
                    data_cat['time_abs(%Y-%m-%dT%H:%M:%S.%f)'].values]
    csv_data = np.array(data_cat['velocity(m/s)'].tolist())

    # Plot in absolute time and save image
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times_dt, csv_data)

    # Customize the plot
    ax.set_xlim((np.min(csv_times_dt), np.max(csv_times_dt)))
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (month-day hour)')
    ax.set_title(f'{test_filename}', fontweight='bold')

    # Plot the arrival time in absolute terms
    arrival_line = ax.axvline(x=arrival_time, c='red', label='Abs. Arrival')
    ax.legend(handles=[arrival_line])

    # Save the plot as image
    plt.savefig(f'{output_directory}{test_filename}_seismic_trace_abs.png')


    # Apply a bandpass filter to highlight certain frequencies (simulated)
    minfreq = 0.5
    maxfreq = 1.0
    filtered_data = csv_data  # Dummy line for filtering

    # Plot the filtered trace and save image
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(csv_times, filtered_data)

    # Mark the detection
    ax.axvline(x=arrival_time_rel, color='red', label='Detection')
    ax.legend(loc='upper left')

    # Customize the plot
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')

    # Save the plot as image
    plt.savefig(f'{output_directory}{test_filename}_filtered_trace.png')


    # Generate a spectrogram and save image
    f, t, sxx = signal.spectrogram(filtered_data, fs=1.0 / (csv_times[1] - csv_times[0]))

    fig = plt.figure(figsize=(10, 10))

    # Time series plot
    ax = plt.subplot(2, 1, 1)
    ax.plot(csv_times, filtered_data)
    ax.axvline(x=arrival_time_rel, color='red', label='Detection')
    ax.legend(loc='upper left')
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')

    # Spectrogram plot
    ax2 = plt.subplot(2, 1, 2)
    vals = ax2.pcolormesh(t, f, sxx, cmap=cm.jet, vmax=5e-17)
    ax2.set_xlim([min(csv_times), max(csv_times)])
    ax2.set_xlabel('Time (Day Hour:Minute)', fontweight='bold')
    ax2.set_ylabel('Frequency (Hz)', fontweight='bold')
    ax2.axvline(x=arrival_time_rel, c='red')
    cbar = plt.colorbar(vals, orientation='horizontal')
    cbar.set_label('Power ((m/s)^2/sqrt(Hz))', fontweight='bold')

    # Save the spectrogram
    plt.savefig(f'{output_directory}{test_filename}_spectrogram.png')


    # Calculate STA/LTA and save characteristic function plot
    sta_len = 30
    lta_len = 150
    cft = classic_sta_lta(csv_data, int(sta_len * (1 / (csv_times[1] - csv_times[0]))),
                          int(lta_len * (1 / (csv_times[1] - csv_times[0]))))

    cft = cft / np.max(cft)  # Normalize the characteristic function

    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    ax.plot(csv_times, cft)
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.set_ylim([0, 10])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Characteristic function')

    # Save the STA/LTA plot
    plt.savefig(f'{output_directory}{test_filename}_characteristic_function.png')


    # Apply the detection threshold for seismic events
    thr_on = 4
    thr_off = 1.5
    on_off = np.array(trigger_onset(cft, thr_on, thr_off))

    # Check if `on_off` has values, otherwise skip the rest of the loop
    if len(on_off) == 0:
        print(f"No triggers found for {test_filename}")
        continue

    # Plot the triggers on the seismic trace and save image
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    for i in np.arange(0, len(on_off)):
        triggers = on_off[i]
        ax.axvline(x=csv_times[triggers[0]], color='red', label=f'Trig. On {i+1}')
        ax.axvline(x=csv_times[triggers[1]], color='purple', label=f'Trig. Off {i+1}')

    ax.plot(csv_times, csv_data)
    ax.set_xlim([min(csv_times), max(csv_times)])
    ax.legend()

    # Save the trigger plot
    plt.savefig(f'{output_directory}{test_filename}_triggers.png')


    # Create a detection catalog
    detection_times = []
    fnames = []

    for i in np.arange(0, len(on_off)):
        triggers = on_off[i]
        on_time = csv_times[triggers[0]] + arrival_time_rel
        on_time_str = datetime.strftime(arrival_time + timedelta(seconds=on_time), '%Y-%m-%dT%H:%M:%S.%f')
        detection_times.append(on_time_str)
        fnames.append(test_filename)

    # Compile the results into a DataFrame
    detect_df = pd.DataFrame(data={'filename': fnames, 'time_abs(%Y-%m-%dT%H:%M:%S.%f)': detection_times,
                                   'time_rel(sec)': csv_times[triggers[0]]})

    # Save the detection catalog to a CSV file
    detect_df.to_csv(f'output/detection_catalog_{test_filename}.csv', index=False)
