from collections import deque

def bfs(r):
    parent = [-1] * (N + 1)
    parent[r] = 0
    q = deque()
    for n_node in alist[r]:
        q.append(n_node)
        parent[n_node] = r

    while q:
        c_node = q.popleft()
        for n_node in alist[c_node]:
            if parent[n_node] != -1: continue
            q.append(n_node)
            parent[n_node] = c_node

    return parent


N = int(input())
alist = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    alist[a].append(b)
    alist[b].append(a)

result = bfs(1)
for i in range(2, N + 1):
    print(result[i])