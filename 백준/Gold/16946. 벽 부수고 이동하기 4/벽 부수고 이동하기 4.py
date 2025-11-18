"""
백준 - 벽 부수고 이동하기 4
"""
from collections import deque, defaultdict

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def counting(y, x, group_num):
    q = deque()
    q.append((y, x))

    cnt = 1
    MAP[y][x] = group_num

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if MAP[ny][nx] != 0: continue
            MAP[ny][nx] = group_num
            q.append((ny, nx))
            cnt += 1

    group[group_num] = cnt


N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
group = defaultdict()
answer = [[0] * M for _ in range(N)]

group_num = 11
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 0:
            counting(y, x, group_num)
            group_num += 1

for y in range(N):
    for x in range(M):
        if MAP[y][x] == 1:
            route_cnt = 0
            area = []
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
                if MAP[ny][nx] == 1: continue
                if MAP[ny][nx] not in area:
                    route_cnt += group[MAP[ny][nx]]
                    area.append(MAP[ny][nx])

            answer[y][x] = (route_cnt + 1) % 10

for a in answer:
    print(*a, sep="")