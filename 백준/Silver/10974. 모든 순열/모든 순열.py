def func(lev):
    if lev == N:
        print(*path)
        return

    for i in range(1, N + 1):
        if visited[i] == 1: continue
        path.append(i)
        visited[i] = 1
        func(lev + 1)
        path.pop()
        visited[i] = 0


N = int(input())

path = []
visited = [0] * (N + 1)
func(0)