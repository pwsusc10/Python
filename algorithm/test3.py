distance = []

house, wifi = map(int, input().split())

for _ in range(house):
    distance.append(int(input()))

distance.sort()

start_node = distance[0]
distance_length = distance[-1] - distance[0]

