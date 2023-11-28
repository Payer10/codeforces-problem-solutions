def find_numbers_summing_to_n(n):
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            z = n - x - y
            if z > y and x % 3 != 0 and y % 3 != 0 and z % 3 != 0:
                return x, y, z
    return None

for i in range(int(input())):
    n = int(input())
    result = find_numbers_summing_to_n(n)

    if result:
        print('YES')
        print(result)
    else:
        print('NO')