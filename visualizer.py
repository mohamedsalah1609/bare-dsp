
import sys
import numpy as np
import sounddevice as sd
import pyqtgraph as pg
from PySide6 import QtWidgets


DEVICE = 6
CHANNELS = 2
SAMPLE_RATE = 48000

duration = int(input("Recording duration (seconds): "))

print("Recording...")

audio = sd.rec(
    int(duration * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    device=DEVICE,
    dtype="float32"
)

sd.wait()

print("Recording finished!")

# Create a time value for every sample
time_axis = np.arange(len(audio)) / SAMPLE_RATE

# Create the application
app = QtWidgets.QApplication(sys.argv)

# Create the main window
window = pg.GraphicsLayoutWidget()
window.setWindowTitle("My Guitar DSP - Waveform Visualizer")
window.resize(1000, 700)

# Left channel graph
left_plot = window.addPlot(
    row=0,
    col=0,
    title="Left Channel"
)

left_plot.setLabel("bottom", "Time", units="s")
left_plot.setLabel("left", "Amplitude")
left_plot.showGrid(x=True, y=True, alpha=0.3)

# Right channel graph
right_plot = window.addPlot(
    row=1,
    col=0,
    title="Right Channel"
)

right_plot.setLabel("bottom", "Time", units="s")
right_plot.setLabel("left", "Amplitude")
right_plot.showGrid(x=True, y=True, alpha=0.3)

# Connect the horizontal axes
right_plot.setXLink(left_plot)

# Draw the waveforms
left_plot.plot(
    time_axis,
    audio[:, 0],
    pen=pg.mkPen(color="cyan", width=1)
)

right_plot.plot(
    time_axis,
    audio[:, 1],
    pen=pg.mkPen(color="orange", width=1)
)

# Display the window
window.show()

sys.exit(app.exec())
