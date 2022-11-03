# 물건의 갯수와 무게
N, W = map(int, input().split())

bag = [[0, 0]]

OPT = [[0 for j in range(W + 1)] for i in range(N + 1)]

value = []

for i in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, N + 1):       # item의 수
    for j in range(1, W + 1):   # 가방의 무게
        if bag[i][0] > j:       # i번째 아이템의 무게가 가방의 허용치보다 크다면
            OPT[i][j] = OPT[i - 1][j]
        else:
            OPT[i][j] = max(OPT[i - 1][j], bag[i][1] + OPT[i-1][j - bag[i][0]])

print(OPT[N][W])
