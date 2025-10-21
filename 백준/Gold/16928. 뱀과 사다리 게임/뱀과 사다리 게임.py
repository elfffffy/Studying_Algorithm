"""
백준 - 뱀과 사다리 게임
"""
import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
routes = [x for x in range(101)]

for _ in range(N):
    start, end = map(int, input().split())
    routes[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    routes[start] = end


def bfs(pos, cnt):
    pq = []
    heapq.heappush(pq, (cnt, pos))
    visited = [0] * 101
    visited[pos] = 1

    while pq:
        c_cnt, c_pos = heapq.heappop(pq)

        if c_pos == 100:
            return c_cnt

        for i in range(1, 7):
            temp = c_pos + i
            if temp > 100: continue
            n_pos = routes[temp]
            if visited[n_pos] == 1: continue
            heapq.heappush(pq, (c_cnt + 1, n_pos))
            visited[n_pos] = 1


min_v = bfs(1, 0)

print(min_v)