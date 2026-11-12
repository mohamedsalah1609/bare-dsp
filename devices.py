import sounddevice as sd

print("Available audio devices:\n")

for i, device in enumerate(sd.query_devices()):
    print(
        f"[{i}] {device['name']}\n"
        f"    Inputs: {device['max_input_channels']}\n"
        f"    Outputs: {device['max_output_channels']}\n"
        f"    Default sample rate: {device['default_samplerate']}\n"
    )

print("Default device:", sd.default.device)