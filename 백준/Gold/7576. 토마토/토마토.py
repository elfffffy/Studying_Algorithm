"""
토마토
"""
from collections import deque

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

q = deque()
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 1:
            q.append((y, x, 0))
            visited[y][x] = 0

        if MAP[y][x] == -1:
            visited[y][x] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

if not q:
    for row in MAP:
        if 1 in row:
            print(0)
            break
    else:
        print(-1)

else:
    while q:
        cy, cx, day = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if MAP[ny][nx] == 0 and visited[ny][nx] == -1:
                q.append((ny, nx, day + 1))
                visited[ny][nx] = day + 1

    for row in visited:
        if -1 in row:
            print(-1)
            break
    else:
        print(max(map(max, visited)))
