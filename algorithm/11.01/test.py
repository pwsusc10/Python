from random import shuffle
from heapq import heapify
import time

stud_id = ["2022"+str(x) for x in range(10000, 20000)]
ranks = [x+1 for x in range(10000)]
shuffle(ranks)

profiles = [(ranks[x], stud_id[x]) for x in range(len(ranks))]

# 우선순위큐로 찾기
start = time.time()
heapify(profiles)
rankers = []
for i in range(3):
    rankers.append(profiles[i])
print(rankers)
end = time.time()
print(end-start, "sec")
