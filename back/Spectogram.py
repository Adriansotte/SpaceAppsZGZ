# %% Generate the spectrogram
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import cm


def create_spectogram(tr_data_filt, tr_filt, tr_times_filt, arrival):
    f, t, sxx = signal.spectrogram(tr_data_filt, tr_filt.stats.sampling_rate)
    fig = plt.figure(figsize=(10, 10))

    # Time series plot
    ax = plt.subplot(2, 1, 1)
    ax.plot(tr_times_filt, tr_data_filt)
    ax.axvline(x=arrival, color='red', label='Detection')
    ax.legend(loc='upper left')
    ax.set_xlim([min(tr_times_filt), max(tr_times_filt)])
    ax.set_ylabel('Velocity (m/s)')
    ax.set_xlabel('Time (s)')

    # Spectrogram plot
    ax2 = plt.subplot(2, 1, 2)
    vals = ax2.pcolormesh(t, f, sxx, cmap=cm.jet, vmax=5e-17)
    ax2.set_xlim([min(tr_times_filt), max(tr_times_filt)])
    ax2.set_xlabel('Time (Day Hour:Minute)', fontweight='bold')
    ax2.set_ylabel('Frequency (Hz)', fontweight='bold')
    ax2.axvline(x=arrival, c='red')
    cbar = plt.colorbar(vals, orientation='horizontal')
    cbar.set_label('Power ((m/s)^2/sqrt(Hz))', fontweight='bold')
    plt.show()

    return fig
