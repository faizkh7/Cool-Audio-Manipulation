import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import math

def findNote(audio, sample_rate):
    # Compute the magnitude spectrum of the audio signal
    X = np.fft.fft(audio)
    X_mag = np.abs(X)
    note_freqs = {}

    # Define the reference frequency for A4 (440 Hz)
    A4_freq = 440.0

    # Define the equal temperament ratio
    equal_temp_ratio = 2 ** (1/12.0)

    # Generate frequencies for all notes from C0 to B8
    for octave in range(9):
        for semitone in range(12):
            note_name = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'][semitone]
            frequency = A4_freq * (equal_temp_ratio ** (octave * 12 + semitone - 57))
            note_freqs[f"{note_name}{octave}"] = frequency
    #print(note_freqs)
    
    detected_notes = ['C0']


    max_freq_index = np.argmax(X_mag)
    max_freq = max_freq_index * sample_rate / len(audio)
    # print(max_freq)
    # print(X_mag)

    # Find the closest note to the detected frequency
    #for i in X_mag:
    f_ratio = sample_rate / len(audio)
    X_mag = X_mag[:len(audio) // 2]  # Only consider the positive frequencies
    #print(audio)
    order = np.array([])
    for i, magnitude in enumerate(X_mag):
        if magnitude>X_mag[max_freq_index]/2:
            frequency = i * f_ratio
            #print(frequency)
            if frequency > 15:
                min_note_diff = float('inf')
                detected_note = None
                for note, freq in note_freqs.items():
                    note_diff = abs(frequency - freq)
                    if note_diff < min_note_diff:
                        min_note_diff = note_diff
                        detected_note = note

                if detected_note != detected_notes[-1]:
                    detected_notes.append(detected_note)
                    order = np.append(order, np.where(audio == magnitude)[0])
                    
    #print(order)
    return detected_notes[1:]

def plot_magnitude_spectrum(signal, sr, title, f_ratio=1):
    X = np.fft.fft(signal)
    X_mag = np.absolute(X)

    plt.figure(figsize=(18, 5))

    f = np.linspace(0, sr, len(X_mag))
    f_bins = int(len(X_mag)*f_ratio)

    plt.plot(f[:f_bins], X_mag[:f_bins])
    plt.xlabel('Frequency (Hz)')
    plt.title(title)
    plt.show()

input_audio1, sample_rate1 = sf.read('a3f5c5.wav')
mono_audio = np.mean(input_audio1, axis=1)


sr = sample_rate1
plot_magnitude_spectrum(mono_audio, sr, "SOUND", 0.1)
print(findNote(mono_audio, sr))
# plot_magnitude_spectrum(piano_audio, sr, "piano", 0.1)
# plot_magnitude_spectrum(sax_audio, sr, "sax", 0.1)
# plot_magnitude_spectrum(noise_audio, sr, "noise", 0.1)



