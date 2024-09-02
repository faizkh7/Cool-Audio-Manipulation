def linear_convolution(input_signal, impulse_response):
    input_length = len(input_signal)
    impulse_length = len(impulse_response)
    output_length = input_length + impulse_length - 1
    output_signal = [0] * output_length

    input_signal += [0] * (output_length - input_length)
    impulse_response += [0] * (output_length - impulse_length)

    for output_index in range(output_length):
        impulse_index = output_index + 1
        temp = 0
        for input_index in range(output_length):
            impulse_index -= 1
            temp += input_signal[input_index] * impulse_response[impulse_index]

            if impulse_index == 0:
                impulse_index += output_length
        output_signal[output_index] = temp

    return output_signal

def main():
    input_signal = [0] * 10
    impulse_response = [0] * 10

    input_length = int(input("\nEnter the length of input signal (L): "))
    print("Enter the values of input signal:")
    input_signal[:input_length] = [float(val) for val in input().split()]

    impulse_length = int(input("\nEnter the length of impulse response (M): "))
    print("Enter the values of impulse response:")
    impulse_response[:impulse_length] = [float(val) for val in input().split()]

    output_length = input_length + impulse_length - 1

    result = linear_convolution(input_signal[:input_length], impulse_response[:impulse_length])

    print("\n\nInput Signal (x[n]):", input_signal[:output_length])
    print("Impulse Response (h[n]):", impulse_response[:output_length])
    print("Output Signal (y[n]):", result[:output_length])
    print("\n")

if __name__ == "__main__":
    main()