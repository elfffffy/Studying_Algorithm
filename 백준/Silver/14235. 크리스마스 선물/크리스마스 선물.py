import heapq

n = int(input())
pq = []
for _ in range(n):
    num_list = list(map(int, input().split()))
    if num_list[0] == 0:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(-1)
    else:
        for p in range(num_list[0]):
            heapq.heappush(pq, -num_list[p + 1])
