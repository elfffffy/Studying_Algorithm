import copy
from collections import deque


def bfs(arr2):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()

    for vy in range(N):
        for vx in range(M):
            if arr2[vy][vx] == 2:
                q.append((vy, vx))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if arr2[ny][nx] != 0: continue

            arr2[ny][nx] = 2
            q.append((ny, nx))

    zero_cnt = 0
    for col in arr2:
        zero_cnt += col.count(0)

    return zero_cnt


def make_arr(lst):
    arr2 = copy.deepcopy(arr)

    a, b, c = lst
    arr2[a[0]][a[1]] = 1
    arr2[b[0]][b[1]] = 1
    arr2[c[0]][c[1]] = 1

    return bfs(arr2)


def combi(lev, start):
    global max_v

    if lev == 3:
        max_v = max(max_v, make_arr(path))
        return

    for i in range(start, len(zero)):
        path.append(zero[i])
        combi(lev + 1, i + 1)
        path.pop()


N, M = map(int, input().split())

# 0 빈칸, 1 벽, 2 바이러스
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
zero = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            zero.append((y, x))

path = []
max_v = float('-inf')
combi(0, 0)
print(max_v)