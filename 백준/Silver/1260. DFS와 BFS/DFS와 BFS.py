from collections import deque

n, m, v = map(int, input().split())
adj_lst = [[] for _ in range(n + 1)]


def bfs(start, visited):
    q = deque()
    q.append(start)

    while q:
        now = q[0]
        print(q.popleft(), end=" ")
        for num in adj_lst[now]:
            if not visited[num]:
                q.append(num)
                visited[num] = True  # 큐에 넣을 떄 밤문 처리


def dfs(start, visited):
    visited[start] = True  # 방문 처리
    print(start, end=" ")

    route = adj_lst[start]
    route.sort()

    for i in range(len(route)):
        t = route[i]
        if not visited[t]:
            dfs(t, visited)
        else:
            continue


for _ in range(m):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

visited = [False] * (n + 1)
dfs(v, visited)
print()
visited = [False] * (n + 1)
visited[v] = True
bfs(v, visited)
