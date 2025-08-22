import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))

pq = []

for i in arr:
    heapq.heappush(pq, i)

cnt = 1

while True:
    if cnt == k:
        print(heapq.heappop(pq))
        break
    else:
        heapq.heappop(pq)
        cnt += 1
