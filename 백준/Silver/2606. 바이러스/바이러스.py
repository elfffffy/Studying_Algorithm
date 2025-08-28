from collections import deque

n = int(input())
m = int(input())


def bfs(t, arr):
    q = deque()
    q.append(t)
    arr[t] = 1

    while q:
        now_n = q.popleft()
        for next_n in connection[now_n]:
            if arr[next_n] == 0:
                q.append(next_n)
                arr[next_n] = 1


connection = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

visited = [0] * (n + 1)
bfs(1, visited)

print(visited.count(1) - 1)
