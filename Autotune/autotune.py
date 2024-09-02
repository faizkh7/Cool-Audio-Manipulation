import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

TEMPO_BPM = 75
ECHO_DURATION_SEC = 0.1
DELAY_AMPLITUDE = 0.5

fs, song_sig_int16 = wavfile.read('path_to_input_file.wav')
song_sig = song_sig_int16.astype(float)/2**15

delay_len_samples = round(ECHO_DURATION_SEC * fs)
impulse_response = np.zeros(delay_len_samples)

impulse_response[0] = 1
impulse_response[-1] = DELAY_AMPLITUDE
ouput_sig = np.convolve(song_sig, impulse_response)

wavfile.write('path_to_output_file.wav', fs, ouput_sig)
print('Autotuned song stored in path_to_output_file.wav')




