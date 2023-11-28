import math
def cr(N):
	if pow(round(N ** (1 / 3)), 3) == N:
		return round(N ** (1 / 3))

	return int(N ** (1 / 3))


def countSC(N):
	res = (int(math.sqrt(N)) + int(cr(N)) - int(math.sqrt(cr(N))))
	return res
if __name__ == "__main__":
    for i in range(int(input())):
        N = int(input())
        print(countSC(N))



