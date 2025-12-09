"""
욕심쟁이 판다
"""

import sys

sys.setrecursionlimit(10 ** 6)


def dfs(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            if MAP[y][x] >= MAP[ny][nx]: continue
            dfs(ny, nx)
            dp[y][x] = max(dp[ny][nx] + 1, dp[y][x])

    else:
        return dp[y][x]


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for y in range(N):
    for x in range(N):
        dfs(y, x)

max_v = -1
for row in dp:
    max_v = max(max_v, max(row))
print(max_v + 1)
