import heapq, sys

input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, num)