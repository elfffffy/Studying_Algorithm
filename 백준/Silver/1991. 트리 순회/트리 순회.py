"""
백준 - 트리 순회
"""


def pre_order(now):
    if graph.get(now) == -1: return
    print(now, end='')
    if graph[now][0] != '.':
        pre_order(graph[now][0])
    if graph[now][1] != '.':
        pre_order(graph[now][1])


def in_order(now):
    if graph.get(now) == -1: return
    if graph[now][0] != '.':
        in_order(graph[now][0])
    print(now, end='')
    if graph[now][1] != '.':
        in_order(graph[now][1])


def post_order(now):
    if graph.get(now) == -1: return
    if graph[now][0] != '.':
        post_order(graph[now][0])
    if graph[now][1] != '.':
        post_order(graph[now][1])
    print(now, end='')


N = int(input())
graph = {}
for _ in range(N):
    root, left, right = input().split()
    graph[root] = [left, right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')