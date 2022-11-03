from heapq import heappop, heappush, heapify

num_list = []
temp_list = []
index1 = 0
index2 = 0
temp = 0

n = int(input())

for _ in range(n):
    heappush(num_list, int(input()))


while len(num_list) > 1:
    index1 = heappop(num_list)
    index2 = heappop(num_list)
    temp = index1 + index2
    heappush(num_list, temp)
    temp_list.append(temp)

print(sum(temp_list))
