# 모듈 Import
from heapq import heappush, heappop

min_heap = []
num_list = []

n = int(input())

for _ in range(n):
    num_list.append(int(input()))

for num in num_list:
    if num == 0:
        if min_heap == []:
            print(0)
        else:
            print(heappop(min_heap))
    else:
        heappush(min_heap, num)
