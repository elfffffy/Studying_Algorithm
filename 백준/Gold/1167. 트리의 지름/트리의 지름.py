"""
백준 - 트리의 지름
트리의 지름 = 두 점 사이의 거리 중 가장 긴 것
"""
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(start, sum_v):
    global dist

    for n_node, n_cost in connection[start]:
        if dist[n_node] == -1:
            dist[n_node] = n_cost + sum_v
            dfs(n_node, n_cost + sum_v)

    return


V = int(input())
connection = [[] for _ in range(V + 1)]

for _ in range(V):
    input_data = list(map(int, input().split()))
    pos = input_data[0]
    for i in range(1, len(input_data), 2):
        node = input_data[i]
        if node == -1: break
        cost = input_data[i + 1]
        connection[pos].append((node, cost))

dist = [-1] * (V + 1)
dist[1] = 0
dfs(1, 0)

farthest_node = 0
farthest_dist = 0
for f_node, f_dist in enumerate(dist):
    if f_dist > farthest_dist:
        farthest_dist = f_dist
        farthest_node = f_node

dist = [-1] * (V + 1)
dist[farthest_node] = 0
dfs(farthest_node, 0)
print(max(dist))