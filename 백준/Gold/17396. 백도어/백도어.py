"""
백준 - 백도어
"""
import heapq, sys

input = sys.stdin.readline


def func(start):
    dist = [float('inf')] * N
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        c_cost, c_pos = heapq.heappop(pq)
        if c_cost > dist[c_pos]: continue
        if c_pos == N - 1:
            return c_cost
        for n_cost, n_pos in alist[c_pos]:
            if sight[n_pos] == 1 and n_pos != N - 1: continue
            total = c_cost + n_cost
            if dist[n_pos] > total:
                dist[n_pos] = total
                heapq.heappush(pq, (total, n_pos))
    return -1


N, M = map(int, input().split())
# 0이면 i번째 분기점이 상대의 시야에 보이지 않는다.
# 1이면 i번째 분기점이 상대의 시야에 보인다.
sight = list(map(int, input().split()))

alist = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    alist[a].append((t, b))
    alist[b].append((t, a))

answer = func(0)
print(answer)