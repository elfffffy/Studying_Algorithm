"""
파핑파핑 지뢰찾기
"""
from collections import deque

# 상 하 좌 우 11시 1시 5시 7시
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]


def check_zero(y, x):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
        if MAP[ny][nx] == '*':
            return False
    return True


def explore(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if visited[ny][nx] == 1: continue

            if check_zero(ny, nx):
                q.append((ny, nx))
                visited[ny][nx] = 1
            else:
                visited[ny][nx] = 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    click = 0

    for y in range(N):
        for x in range(N):
            if MAP[y][x] == '.':
                if visited[y][x] == 1: continue
                if check_zero(y, x):
                    explore(y, x, visited)
                    click += 1

    for vy in range(N):
        for vx in range(N):
            if visited[vy][vx] == 1: continue
            if MAP[vy][vx] == '*': continue
            click += 1

    print(f'#{tc} {click}')
