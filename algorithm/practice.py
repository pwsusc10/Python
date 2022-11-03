# 비구조할당
# filter, list comprehension, for loop, map, lamda, deque

# a = int(input())
# b = int(input())

# print(a, b)

# n, m = map(int, input().split())

# for i in range(n):
#     list_temp = list(map(int, input().split()))
#     for indx , number in enumerate(list_temp):
#         print(indx, number)

list1 = list(map((lambda x: x + x), input().split()))
print(list1)

# 소스 행렬 입력받기
for i in range(N):
    list_temp = list(map(int, list(input())))
    source.append(list_temp)
