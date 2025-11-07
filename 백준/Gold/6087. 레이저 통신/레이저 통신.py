"""
레이저 통신
. 빈칸 / * 벽
"""
from collections import deque


def bfs(sy, sx):
    q = deque()

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    visited = [[[float('inf')] * 4 for _ in range(M)] for _ in range(N)]

    for d in range(4):
        q.append((sy, sx, d, 0))
        visited[sy][sx][d] = 0

    while q:
        cy, cx, c_dir, cnt = q.popleft()

        if cy == target_y and cx == target_x: continue

        if cnt > visited[cy][cx][c_dir]: continue

        ny = cy + dy[c_dir]
        nx = cx + dx[c_dir]

        if 0 <= ny < N and 0 <= nx < M:
            if MAP[ny][nx] != '*':
                if visited[ny][nx][c_dir] > cnt:
                    visited[ny][nx][c_dir] = cnt
                    q.append((ny, nx, c_dir, cnt))

        for n_dir in range(4):
            if n_dir == c_dir: continue
            if abs(n_dir - c_dir) == 2: continue

            ny = cy + dy[n_dir]
            nx = cx + dx[n_dir]

            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] != '*':
                    if visited[ny][nx][n_dir] > cnt + 1:
                        visited[ny][nx][n_dir] = cnt + 1
                        q.append((ny, nx, n_dir, cnt + 1))

    return min(visited[target_y][target_x])


M, N = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
pos = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'C':
            pos.append((y, x))

start_y, start_x = pos[0][0], pos[0][1]
target_y, target_x = pos[1][0], pos[1][1]

result = bfs(start_y, start_x)

print(result)