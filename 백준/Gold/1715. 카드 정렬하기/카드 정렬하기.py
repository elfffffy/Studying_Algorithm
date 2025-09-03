import heapq, sys

input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    heapq.heappush(pq, int(input()))

answer = []
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    heapq.heappush(pq, a + b)
    answer.append(a + b)

print(sum(answer))