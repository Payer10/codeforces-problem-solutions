def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))

        arr_ind = 0
        inc_value = 1
        count = 0
        ans = 0

        while count != n:
            if arr[arr_ind] != inc_value and inc_value > ans:
                arr_ind += 1
                ans = inc_value
                count += 1
            inc_value += 1

        print(ans)

if __name__ == "__main__":
    main()
