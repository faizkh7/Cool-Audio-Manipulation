import math

def dft(N, a, b, A, B):
    omega = 2 * math.pi / N

    for k in range(N):
        A[k] = 0
        B[k] = 0

        for n in range(N):
            arg = omega * k * n
            c = math.cos(arg)
            d = math.sin(arg)

            A[k] += a[n] * c + b[n] * d
            B[k] += -a[n] * d + b[n] * c

def idft(N, A, B, a, b):
    omega = 2 * math.pi / N

    for k in range(N):
        a[k] = 0
        b[k] = 0

        for i in range(N):
            arg = omega * k * i
            c = math.cos(arg)
            d = math.sin(arg)

            a[k] += A[i] * c - B[i] * d
            b[k] += A[i] * d + B[i] * c

        a[k] /= N
        b[k] /= N

def main():
    
    N = int(input("Enter the length of x[n] ie N = "))
    a = [0] * N
    b = [0] * N
    A = [0] * N
    B = [0] * N

    print("Enter the values of x[n]: ")
    for i in range(N):
        a[i] = float(input())

    # DFT
    dft(N, a, b, A, B)

    print("X[k] by DFT: ")
    for i in range(N):
        print(f"{A[i]:.2f} + j {B[i]:.2f}")

    # IDFT
    idft(N, A, B, a, b)
    print()
    print("x[n] by IDFT: ")
    for i in range(N):
        print(f"{a[i]:.2f} + j {b[i]:.2f}")

if __name__ == "__main__":
    main()
