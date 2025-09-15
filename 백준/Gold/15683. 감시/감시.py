"""
백준 - 감시
"""
import copy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
CCTV = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 2, 3], [0, 1, 3], [1, 2, 3], [2, 1, 0]],
    [[0, 1, 2, 3]]
]


def check(cy, cx, cctv, arr):
    for way in cctv:
        ny, nx = cy, cx
        while True:
            ny += dy[way]
            nx += dx[way]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: break
            if arr[ny][nx] == 6: break
            if arr[ny][nx] == 0:
                arr[ny][nx] = '#'
    return


def func(lev, arr):
    global min_v

    if lev == len(cctv_lst):
        cnt = 0
        for row in arr:
            cnt += row.count(0)

        min_v = min(cnt, min_v)
        return

    cy, cx, c_type = cctv_lst[lev]
    for cctv in CCTV[c_type]:
        MAP2 = copy.deepcopy(arr)
        check(cy, cx, cctv, MAP2)
        func(lev + 1, MAP2)


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

cctv_lst = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] != 0 and MAP[y][x] != 6:
            cctv_lst.append((y, x, MAP[y][x]))

min_v = float('inf')
func(0, MAP)
print(min_v)