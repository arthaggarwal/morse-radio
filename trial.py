import numpy as np
import matplotlib.pyplot as plt

# Assume we have already defined the necessary functions like `pulse_index_to_start_t` and `tone`

# Example Morse code pulse (binary string)
pulses = '10001011100011100000001000000011101010100010111000111'

# Settings
pulse_duration = 0.1  # Example: duration of each pulse (in seconds)
samp_rate = 44100  # Sampling rate in Hz (samples per second)
sound_freq = 1000  # Frequency of the tone in Hz
sound_amplitude = 0.5  # Amplitude of the tone

# Define the function to calculate the time range for an "on-pulse"
def get_on_pulse_time_range(pulse_index):
    # Assuming pulse_duration is given for each pulse
    start_t = pulse_index * pulse_duration  # Pulse starts at index * pulse_duration
    end_t = (pulse_index + 1) * pulse_duration  # Pulse ends at the next index * pulse_duration
    return start_t, end_t

# Define the function to generate the tone for each pulse (simple sinusoidal tone)
def generate_tone(start_t, end_t, sound_freq, sound_amplitude):
    t_values = np.linspace(start_t, end_t, int((end_t - start_t) * samp_rate))  # time array for the pulse
    tone_samples = sound_amplitude * np.sin(2 * np.pi * sound_freq * t_values)  # Sinusoidal signal
    return t_values, tone_samples

# Choose a pulse index to visualize (e.g., the first 'on' pulse)
pulse_index = 1  # For example, the second pulse
start_t, end_t = get_on_pulse_time_range(pulse_index)

# Generate the tone for the selected "on-pulse"
t_values, tone_samples = generate_tone(start_t, end_t, sound_freq, sound_amplitude)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t_values, tone_samples, label='Tone Signal')

# Zoom into the "on-pulse" using xlim and ylim
plt.xlim([start_t, end_t])  # Zoom into the time range of the "on-pulse"
plt.ylim([min(tone_samples), max(tone_samples)])  # Zoom into the signal range

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Signal (arbitrary units)')
plt.title('On-Pulse Signal')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
