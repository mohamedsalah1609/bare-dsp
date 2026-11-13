
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 48000
CHANNELS = 2
BLOCK_SIZE = 512

INPUT_DEVICE = 7
OUTPUT_DEVICE = 9


def audio_callback(indata, outdata, frames, time, status):

    if status:
        print(status)

    outdata[:] = 7 * indata


print("Starting live audio...")

with sd.Stream(
    samplerate=SAMPLE_RATE,
    blocksize=BLOCK_SIZE,
    channels=CHANNELS,
    dtype="float32",
    device=(INPUT_DEVICE, OUTPUT_DEVICE),
    callback=audio_callback
):

    print("Live audio is running. Press Ctrl+C to stop.")

    try:
        while True:
            sd.sleep(1000)

    except KeyboardInterrupt:
        print("\nStopping audio...")
