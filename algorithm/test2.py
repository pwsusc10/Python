from itertools import combinations

distance = []
# temp_list = []

house, wifi = map(int, input().split())

for _ in range(house):
    distance.append(int(input()))

distance.sort()

# 첫번째 노드와 마지막 노드 저장
start_node = distance[0]
end_node = distance[-1]

# 첫번쨰 노드와 마지막 노드 삭제
distance.pop()
del distance[0]

for temp_list in combinations(distance, wifi - 2):
    temp_list = list(temp_list)
    temp_list.append(start_node)
    temp_list.append(end_node)
    print(temp_list)
