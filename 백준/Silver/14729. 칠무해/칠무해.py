import heapq, sys

input = sys.stdin.readline

n = int(input())  # 학생 수
pq = []

for _ in range(n):
    num = float(input())
    heapq.heappush(pq, num)

while len(pq) > n - 7:
    print(f'{heapq.heappop(pq):.3f}')