import math

def DITFFT_4_Point(N, x, t):
    G = [[0, 0] for _ in range(4)]
    H = [[0, 0] for _ in range(4)]

    # Stage-1
    G[0][0] = x[0][0] + x[2][0]
    G[0][1] = x[0][1] + x[2][1]
    G[1][0] = x[0][0] - x[2][0]
    G[1][1] = x[0][1] - x[2][1]
    H[0][0] = x[1][0] + x[3][0]
    H[0][1] = x[1][1] + x[3][1]
    H[1][0] = x[1][0] - x[3][0]
    H[1][1] = x[1][1] - x[3][1]

    # Stage-2
    e = 6.283185307179586 / N

    # X[k] = G[k] + WNnk H[k]
    k = 0
    t[0][0] = G[0][0] + (H[0][0] * math.cos(e * k) + H[0][1] * math.sin(e * k))
    t[0][1] = G[0][1] + (H[0][1] * math.cos(e * k) - H[0][0] * math.sin(e * k))

    k = 1
    t[1][0] = G[1][0] + (H[1][0] * math.cos(e * k) + H[1][1] * math.sin(e * k))
    t[1][1] = G[1][1] + (H[1][1] * math.cos(e * k) - H[1][0] * math.sin(e * k))

    k = 2
    t[2][0] = G[0][0] + (H[0][0] * math.cos(e * k) + H[0][1] * math.sin(e * k))
    t[2][1] = G[0][1] + (H[0][1] * math.cos(e * k) - H[0][0] * math.sin(e * k))

    k = 3
    t[3][0] = G[1][0] + (H[1][0] * math.cos(e * k) + H[1][1] * math.sin(e * k))
    t[3][1] = G[1][1] + (H[1][1] * math.cos(e * k) - H[1][0] * math.sin(e * k))

def DITFFT_8_Point(N, x, t):
    G = [[0, 0] for _ in range(4)]
    H = [[0, 0] for _ in range(4)]
    X1 = [[0, 0] for _ in range(4)]
    X2 = [[0, 0] for _ in range(4)]

    for i in range(4):
        X1[i][0] = x[2 * i][0]
        X1[i][1] = x[2 * i][1]
        X2[i][0] = x[2 * i + 1][0]
        X2[i][1] = x[2 * i + 1][1]

    DITFFT_4_Point(4, X1, G)
    DITFFT_4_Point(4, X2, H)

    e = 6.283185307179586 / N

    for k in range(4):
        t[k][0] = G[k][0] + (H[k][0] * math.cos(e * k) + H[k][1] * math.sin(e * k))
        t[k][1] = G[k][1] + (H[k][1] * math.cos(e * k) - H[k][0] * math.sin(e * k))

    for k in range(4):
        d = k + 4
        t[d][0] = G[k][0] + (H[k][0] * math.cos(e * d) + H[k][1] * math.sin(e * d))
        t[d][1] = G[k][1] + (H[k][1] * math.cos(e * d) - H[k][0] * math.sin(e * d))

if __name__ == "__main__":
    L = 4
    N = 8 if L > 4 else 4

    x = [[0, 0] for _ in range(N)]
    X = [[0, 0] for _ in range(N)]
    t = [[0, 0] for _ in range(N)]

    print("\nEnter the values of x[n]: ")
    for i in range(L):
        x[i][0] = float(input())

    print("\nInput signal x[n] = ")
    for i in range(L):
        print(f"  {x[i][0]:.3f}  ")

    if N == 4:
        DITFFT_4_Point(N, x, X)
    elif N == 8:
        DITFFT_8_Point(N, x, X)
    else:
        exit(0)

    print("\nFFT results X[k]: ")
    for k in range(N):
        print(f"\n {X[k][0]:.3f} + j {X[k][1]:.3f}")

    for i in range(N):
        x[i][0] = 0
        x[i][1] = 0

    for k in range(N):
        X[k][1] = X[k][1] * (-1)

    if N == 4:
        DITFFT_4_Point(N, X, x)
    elif N == 8:
        DITFFT_8_Point(N, X, x)
    else:
        exit(0)

    for n in range(N):
        x[n][0] = x[n][0] / N
        x[n][1] = -x[n][1] / N

    print("\nInverse FFT results x[n]: ")
    for n in range(N):
        print(f"\n {x[n][0]:.3f} + j {x[n][1]:.3f}\n")
