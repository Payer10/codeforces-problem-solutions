def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def main():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        ans = True
        poly_s = 0
        poly_e = 0

        for _ in range(n):
            s, e = map(int, input().split())
            if poly_s == 0:
                poly_s = s
                poly_e = e
            else:
                if s >= poly_s and e >= poly_e:
                    ans = False

        if ans:
            print(poly_s)
        else:
            print(-1)

if __name__ == "__main__":
    main()
