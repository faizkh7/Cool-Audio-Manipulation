import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

#generated using matplotlib.pyplot
kernel = np.array(
    [-0.0003, 0.0000, 0.0003, 0.0005, 0.0006, 0.0005, 0.0002, -0.0003, -0.0008, -0.0011, -0.0012, -0.0008, 0.0000,
     0.0010, 0.0019, 0.0024, 0.0020, 0.0008, -0.0009, -0.0028, -0.0040, -0.0041, -0.0027, 0.0000, 0.0033, 0.0060,
     0.0072, 0.0060, 0.0025, -0.0027, -0.0079, -0.0113, -0.0114, -0.0074, 0.0000, 0.0089, 0.0165, 0.0197, 0.0167,
     0.0069, -0.0077, -0.0233, -0.0347, -0.0367, -0.0255, 0.0000, 0.0375, 0.0817, 0.1252, 0.1599, 0.1791, 0.1791,
     0.1599, 0.1252, 0.0817, 0.0375, 0.0000, -0.0255, -0.0367, -0.0347, -0.0233, -0.0077, 0.0069, 0.0167, 0.0197,
     0.0165, 0.0089, 0.0000, -0.0074, -0.0114, -0.0113, -0.0079, -0.0027, 0.0025, 0.0060, 0.0072, 0.0060, 0.0033,
     0.0000, -0.0027, -0.0041, -0.0040, -0.0028, -0.0009, 0.0008, 0.0020, 0.0024, 0.0019, 0.0010, 0.0000, -0.0008,
     -0.0012, -0.0011, -0.0008, -0.0003, 0.0002, 0.0005, 0.0006, 0.0005, 0.0003, 0.0000, -0.0003])


#convolution using formula: SUMMATION -> x(m)h(n-m)
def custom_convolve(signal, kernel=kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    output = np.zeros(signal_len)
    for i in range(signal_len):
        for j in range(kernel_len):
            if i - j >= 0:
                output[i] += signal[i - j] * kernel[j]

    return output


input_audio, sample_rate = sf.read('path_to_input_audio')
print(sample_rate)


denoised_audio = custom_convolve(input_audio, kernel)

#Normalizing the denoised audio by dividing it by the maximum absolute value of the denoised signal is a common practice in signal processing and audio processing. This step is performed to ensure that the denoised audio maintains the same amplitude range as the original audio and to prevent clipping or distortion in the output.
denoised_audio = denoised_audio / np.max(np.abs(denoised_audio))


#plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title("Noisy Audio")
plt.plot(input_audio)
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.title("Denoised Audio")
plt.plot(denoised_audio)
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

#saving new sound
print("Before creation")
sf.write('path_to_denoise', denoised_audio,sample_rate)
print("After creation")
print("Denoising completed and saved to 'path_to_denoise'")
