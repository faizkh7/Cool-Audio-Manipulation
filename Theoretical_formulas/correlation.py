def custom_correlate(signal1, signal2):
    length1 = len(signal1)
    length2 = len(signal2)

    def custom_detect(array):
        i = 0
        s = 0
        while s == 0 and i < len(array):
            if array[i] != 0:
                s = 1
            i += 1
        return i - 1, len(array) - i + 1

    start_index1, length1 = custom_detect(signal1)
    start_index2, length2 = custom_detect(signal2)

    negative_count = start_index2 - start_index1 + length2 - 1
    positive_count = length1 - (start_index2 - start_index1)

    result = [0] * (length1 + length2 - 1)

    for i in range(-negative_count, positive_count):
        temp = 0
        for j in range(start_index1, start_index1 + length1):
            if 0 <= j - i < len(signal2):
                temp += signal1[j] * signal2[j - i]
        result[i] = temp

    return result[:(positive_count - 1) + length2]

def main():
    SIZE = 20
    OFFSET = 10
    x = [0] * SIZE
    h = [0] * SIZE
    y = [0] * SIZE

    print("Enter the length of x[n]: ", end="")
    length1 = int(input())
    print("Enter values for x[n]: ", end="")
    values = input().split()
    for i in range(length1):
        x[OFFSET + i] = float(values[i])

    print("Enter the length of h[n]: ", end="")
    length2 = int(input())
    print("Enter values for h[n]: ", end="")
    values = input().split()
    for i in range(length2):
        h[OFFSET + i] = float(values[i])

    result = custom_correlate(x, h)
    print()
    print("y =", end=" ")
    for value in result:
        print(f"{value:.2f}", end=" ")
    print("\n")

if __name__ == "__main__":
    main()
