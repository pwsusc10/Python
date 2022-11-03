def find_num(num_list, idx):
    cnt = 0
    for i in range(idx + 1, len(num_list)):
        if num_list[idx] < num_list[i]:
            cnt += 1
    return cnt


N = int(input())
array = list(map(int, input().split()))


start_idx = -1
temp_max = -1
temp_idx = 0
cnt = 0
ex_num = 0

while (True):
    for idx in range(start_idx + 1, len(array)):
        if array[idx] <= ex_num:
            continue
        if find_num(array, idx) >= temp_max:
            temp_max = find_num(array, idx)
            temp_idx = idx

    cnt += 1

    if find_num(array, temp_idx) == 0:
        break
    start_idx = temp_idx
    ex_num = array[start_idx]

    temp_max = 0

print(cnt)
