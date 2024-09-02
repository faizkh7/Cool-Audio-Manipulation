import numpy as np

def circular_convolution(x, h):
    N = len(x)
    y = np.zeros(N)
    h = np.roll(h[::-1], 1)

    for s in range(N):
        signal = np.roll(h, s)
        y[s] = np.sum(x * signal)

    return y

def main():
    max_len = 64
    x = np.zeros(max_len)
    h = np.zeros(max_len)

    L = int(input("Enter the length of x[n] (L): "))
    x_values = input().split()
    x[:L] = [float(val) for val in x_values]

    M = int(input("Enter the length of h[n] (M): "))
    h_values = input().split()
    h[:M] = [float(val) for val in h_values]

    N = max(L, M)
    result = circular_convolution(x[:N], h[:N])

    print("\n\n x[n] =", x[:N])
    print("\n\n h[n] =", h[:N])
    print("\n\n y[n] =", result[:N])
    print("\n")

if __name__ == "__main__":
    main()
