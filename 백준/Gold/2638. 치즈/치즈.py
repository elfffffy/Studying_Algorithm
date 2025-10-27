"""
백준 - 치즈
"""
from collections import deque


def outer(y, x):
    q = deque()
    q.append((y, x))
    space = [[0] * M for _ in range(N)]
    space[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if MAP[ny][nx] == 1: continue
            if space[ny][nx] == 1: continue
            q.append((ny, nx))
            space[ny][nx] = 1

    return space


def check(y, x):
    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if outer_space[ny][nx] == 1:
            cnt += 1
    if cnt >= 2:
        MAP[y][x] = 0


# 입력값 받기
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

hours = 0
while True:
    for row in MAP:
        if 1 in row:
            break
    else:
        break

    outer_space = outer(0, 0)
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if MAP[y][x] == 1:
                check(y, x)
    hours += 1

print(hours)