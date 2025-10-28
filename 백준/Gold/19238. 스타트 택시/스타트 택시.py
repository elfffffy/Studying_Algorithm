"""
백준 - 스타트 택시
"""
import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs_passengers(taxi_y, taxi_x):
    global F

    if (taxi_y, taxi_x) in passengers:
        return taxi_y, taxi_x

    q = deque()
    q.append((0, taxi_y, taxi_x))
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[taxi_y][taxi_x] = 1
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    min_dist = float('inf')
    next_y, next_x = 0, 0

    while q:
        cnt, cy, cx = q.popleft()

        if cnt > min_dist: break

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 1 or nx < 1 or ny >= N + 1 or nx >= N + 1: continue
            if MAP[ny][nx] == 1: continue
            if visited[ny][nx] == 1: continue
            if (ny, nx) in passengers:
                if min_dist > cnt + 1:
                    min_dist = cnt + 1
                    next_y, next_x = ny, nx
                elif min_dist == cnt + 1:
                    if next_y > ny or (next_y == ny and next_x > nx) :
                        next_y, next_x = ny, nx
            q.append((cnt + 1, ny, nx))
            visited[ny][nx] = 1

    if min_dist == float('inf'):
        return -1, -1
    F -= min_dist
    if F < 0:
        return -1, -1
    return next_y, next_x


def bfs_goal(py, px, goal_y, goal_x):
    global F

    if (py, px) == (goal_y, goal_x):
        return py, px

    q = deque()
    q.append((0, py, px))
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[py][px] = 1
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    while q:
        cnt, cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 1 or nx < 1 or ny >= N + 1 or nx >= N + 1: continue
            if MAP[ny][nx] == 1: continue
            if visited[ny][nx] == 1: continue
            if (ny, nx) == (goal_y, goal_x):
                F -= (cnt + 1)
                if F < 0:
                    return -1, -1
                F += (cnt + 1) * 2
                return ny, nx
            q.append((cnt + 1, ny, nx))
            visited[ny][nx] = 1

    return -1, -1


N, M, F = map(int, input().split())
MAP = [[0] * (N + 1)]
for _ in range(N):
    data = list(map(int, input().split()))
    MAP.append([0] + data)
taxi_y, taxi_x = map(int, input().split())
passengers = [()]
goal = [()]
complete = [0] + [1] * M

for _ in range(1, M + 1):
    data = list(map(int, input().split()))
    passengers.append((data[0], data[1]))
    goal.append((data[2], data[3]))

while True:
    if 1 not in complete:
        break

    py, px = bfs_passengers(taxi_y, taxi_x)
    if (py, px) == (-1, -1):
        F = -1
        break

    for i in range(1, M + 1):
        if (py, px) == passengers[i]:
            passengers_num = i
            break
    passengers[i] = (0, 0)
    goal_y, goal_x = goal[i]
    taxi_y, taxi_x = bfs_goal(py, px, goal_y, goal_x)
    if (taxi_y, taxi_x) == (-1, -1):
        F = -1
        break
    complete[i] = 0
    goal[i] = (0, 0)

print(F)