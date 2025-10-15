"""
백준 - 불!
"""
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def fire(fire_pos, c):
    global fire_cnt

    q = deque()
    for fire_y, fire_x in fire_pos:
        q.append((fire_y, fire_x, c))
        fire_cnt[fire_y][fire_x] = c

    while q:
        fy, fx, cnt = q.popleft()

        for i in range(4):
            n_fy = fy + dy[i]
            n_fx = fx + dx[i]

            if n_fx < 0 or n_fy < 0 or n_fx >= M or n_fy >= N: continue
            if MAP[n_fy][n_fx] == '#': continue
            if fire_cnt[n_fy][n_fx] != -1: continue
            q.append((n_fy, n_fx, cnt + 1))
            fire_cnt[n_fy][n_fx] = cnt + 1


def jihoon(c):
    global jihoon_visited

    q = deque()
    q.append((c, jihoon_y, jihoon_x))
    jihoon_visited[jihoon_y][jihoon_x] = 1

    while q:
        cnt, jy, jx = q.popleft()

        if jy == 0 or jy == N - 1 or jx == 0 or jx == M - 1:
            return cnt + 1

        for i in range(4):
            n_jy = jy + dy[i]
            n_jx = jx + dx[i]

            if n_jx < 0 or n_jy < 0 or n_jx >= M or n_jy >= N: continue
            if jihoon_visited[n_jy][n_jx] == 1: continue
            if MAP[n_jy][n_jx] == '#': continue
            if fire_cnt[n_jy][n_jx] != -1 and fire_cnt[n_jy][n_jx] <= cnt + 1: continue

            q.append((cnt + 1, n_jy, n_jx))
            jihoon_visited[n_jy][n_jx] = 1

    return 'IMPOSSIBLE'


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]

jihoon_x, jihoon_y = 0, 0
fire_pos = []

for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'J':
            jihoon_y, jihoon_x = y, x

        elif MAP[y][x] == 'F':
            fire_pos.append((y, x))

fire_cnt = [[-1] * M for _ in range(N)]
fire(fire_pos, 0)

jihoon_visited = [[0] * M for _ in range(N)]
answer = jihoon(0)

print(answer)