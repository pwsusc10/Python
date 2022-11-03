# 모듈 Import
from heapq import heappush, heappop

min_heap = []
num_list = []

n = int(input())

for _ in range(n):
    temp = int(input())
    num_list.append(temp * -1)

for num in num_list:
    if num == 0:
        if min_heap == []:
            print(0)
        else:
            print(heappop(min_heap) * -1)
    else:
        heappush(min_heap, num)
