import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())


def dfs(y, x):
    global cnt

    arr[y][x] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if arr[ny][nx] == 1:
            dfs(ny, nx)


for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    arr = [[0] * M for i in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)
