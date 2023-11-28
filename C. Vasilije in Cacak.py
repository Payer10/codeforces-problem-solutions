# Define a function to calculate the GCD
def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

# Main function
def main():
    tes = int(input())
    for _ in range(tes):
        n, k, x = map(int, input().split())
        sum = (k * (k + 1)) // 2  # Use integer division in Python to get an integer result
        different = (n * k) - (k * (k - 1)) // 2  # Use integer division
        if sum <= x and different >= x:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
