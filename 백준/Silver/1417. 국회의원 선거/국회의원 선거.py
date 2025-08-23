import heapq

N = int(input())  # 후보의 수

num_1 = int(input())
arr = [int(input()) for _ in range(N - 1)]
cnt = 0

pq = []

for a in arr:
    heapq.heappush(pq, -a)

while pq and num_1 <= -pq[0]:
    num = -heapq.heappop(pq)
    num -= 1
    num_1 += 1
    cnt += 1
    heapq.heappush(pq, -num)

print(cnt)