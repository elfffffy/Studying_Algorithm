"""
백준 - 문제집
"""
import heapq, sys

input = sys.stdin.readline

# N : 문제의 수
# M : 정보의 개수
N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    in_degree[b] += 1
    graph[a].append(b)

pq = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    c_node = heapq.heappop(pq)
    print(c_node, end=" ")
    for n_node in graph[c_node]:
        in_degree[n_node] -= 1
        if in_degree[n_node] == 0:
            heapq.heappush(pq, n_node)