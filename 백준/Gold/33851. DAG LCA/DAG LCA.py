"""
백준 - DAG LCA
"""
import sys

from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


# [[], [], [1], [1], [3], [2, 4]]

def Find(u, lev, lst):
    if graph[u]:
        for n_node in graph[u]:
            Find(n_node, lev + 1, lst)
    lst[u] = min(lev, lst[u])


for _ in range(Q):
    u, v = map(int, input().split())
    route_u = [float('inf')] * (N + 1)
    route_v = [float('inf')] * (N + 1)

    Find(u, 0, route_u)
    Find(v, 0, route_v)

    result = float('inf')
    for i in range(1, N + 1):
        if route_v[i] != float('inf') and route_u[i] != float('inf'):
            result = min(result, max(route_v[i], route_u[i]))

    if result == float('inf'):
        print(-1)
    else:
        print(result)