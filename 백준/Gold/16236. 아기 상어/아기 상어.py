"""
백준 - 아기 상어
"""
import heapq
from collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
my_fish_y, my_fish_x = 0, 0
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 9:
            my_fish_y, my_fish_x = y, x

# 상 좌 하 우
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def eat_fish(cnt):
    q = deque()
    q.append((cnt, my_fish_y, my_fish_x))
    MAP[my_fish_y][my_fish_x] = 0
    visited = [[0] * N for _ in range(N)]
    visited[my_fish_y][my_fish_x] = 1
    fishes = []

    while q:
        c_cnt, cy, cx = q.popleft()

        if 0 < MAP[cy][cx] < my_size:
            fishes.append((c_cnt, cy, cx))

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if MAP[ny][nx] > my_size: continue
            if visited[ny][nx] == 1: continue
            q.append((c_cnt + 1, ny, nx))
            visited[ny][nx] = 1

    if fishes:
        fishes.sort()
        return fishes[0]
    else:
        return 0


total = 0
my_size = 2
eating = 0
while True:
    result = eat_fish(0)
    if result == 0:
        break
    else:
        total += result[0]
        eating += 1
        if eating == my_size:
            eating = 0
            my_size += 1
        my_fish_y, my_fish_x = result[1], result[2]
        MAP[my_fish_y][my_fish_x] = 0

print(total)