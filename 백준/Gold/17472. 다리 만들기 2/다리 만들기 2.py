"""
백준 - 다리 만들기 2
"""
from collections import deque


def Find(x):
    if boss[x] == x:
        return x
    boss[x] = Find(boss[x])
    return boss[x]


def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)

    if a == b:
        return

    boss[b] = a
    return


# N: 세로 M: 가로
N, M = map(int, input().split())

# 0: 바다, 1: 땅
MAP = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def is_outline(cy, cx):
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if MAP[ny][nx] == 0:
            return True
    return False


def func(y, x):
    q = deque()
    q.append((y, x))
    MAP[y][x] = spot
    while q:
        now = q.popleft()
        cy, cx = now[0], now[1]
        if is_outline(cy, cx):
            islands[spot].append((cy, cx))
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if MAP[ny][nx] == 1:
                MAP[ny][nx] = spot
                q.append((ny, nx))


islands = [[] for _ in range(9)]
spot = 2
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 1:
            func(y, x)
            spot += 1


def make_bridges(sy, sx):
    for i in range(4):
        ny, nx = sy, sx
        cnt = 0
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: break
            if MAP[ny][nx] == MAP[sy][sx]: break
            if MAP[ny][nx] == 0:
                cnt += 1
            else:
                if cnt >= 2:
                    i1 = MAP[sy][sx]
                    i2 = MAP[ny][nx]
                    if i1 < i2:
                        bridges.add((cnt, i1, i2))
                        
                break


bridges = set()
for island in islands[2:]:
    for sy, sx in island:
        make_bridges(sy, sx)

sorted_bridges = sorted(list(bridges))
boss = [x for x in range(spot)]
answer = 0
cnt = 0

for cost, t1, t2 in sorted_bridges:
    if Find(t1) != Find(t2):
        Union(t1, t2)
        answer += cost
        cnt += 1

    if cnt > spot - 3:
        break

if cnt == spot - 3:
    print(answer)
else:
    print(-1)