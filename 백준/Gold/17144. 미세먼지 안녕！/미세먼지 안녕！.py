"""
미세먼지 안녕!
"""

import sys

input = sys.stdin.readline

N, M, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

air_top_y = 0
air_bottom_y = 0

for y in range(N):
    if MAP[y][0] == -1:
        air_top_y = y
        air_bottom_y = y + 1
        break

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while True:
    if T == 0: break

    new_map = [[0] * M for _ in range(N)]
    new_map[air_top_y][0] = -1
    new_map[air_bottom_y][0] = -1

    # 먼지 퍼지기
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == -1 or MAP[y][x] == 0: continue

            dust = MAP[y][x]
            spread_dust = dust // 5
            cnt = 0

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
                if MAP[ny][nx] == -1: continue
                new_map[ny][nx] += spread_dust
                cnt += 1

            new_map[y][x] = new_map[y][x] + (dust - (spread_dust * cnt))

    new_map[air_top_y][0] = 0
    new_map[air_bottom_y][0] = 0
    temp = [row[:] for row in new_map]

    # 반시계 방향 회전
    for x in range(1, M):
        new_map[air_top_y][x] = temp[air_top_y][x - 1]

    for y in range(air_top_y - 1, -1, -1):
        new_map[y][M - 1] = temp[y + 1][M - 1]

    for x in range(M - 1):
        new_map[0][x] = temp[0][x + 1]

    for y in range(1, air_top_y):
        new_map[y][0] = temp[y - 1][0]

    # 시계 방향 회전
    for x in range(1, M):
        new_map[air_bottom_y][x] = temp[air_bottom_y][x - 1]

    for y in range(air_bottom_y + 1, N):
        new_map[y][M - 1] = temp[y - 1][M - 1]

    for x in range(M - 1):
        new_map[N - 1][x] = temp[N - 1][x + 1]

    for y in range(air_bottom_y, N - 1):
        new_map[y][0] = temp[y + 1][0]

    T -= 1
    new_map[air_top_y][0] = -1
    new_map[air_bottom_y][0] = -1

    MAP = new_map

print(sum(map(sum, MAP)) + 2)
