import sounddevice as sd
import numpy as np


DEVICE = 6
CHANNELS = 2
SAMPLE_RATE = 48000

duration = int(input("recording duration (in seconds): "))

print("Recording... play your guitar!")

audio = sd.rec(
    int(duration * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    device=DEVICE,
    dtype="float32"
)
sd.wait()

print("Recording finished!")

print("\nFirst 10 frames:")
print(audio[:10])

print("\nArray information:")
print("Shape:", audio.shape)
print("Data type:", audio.dtype)
print("Size:", audio.nbytes, "bytes")

print("\nPeak amplitude:")
print(np.max(np.abs(audio), axis=0))

print("\nPlaying recording...")

sd.play(audio, samplerate=SAMPLE_RATE, device=DEVICE)
sd.wait()

print("Playback finished!")