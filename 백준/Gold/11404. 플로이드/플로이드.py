"""
백준 - 플로이드
"""
N = int(input())
M = int(input())
MAP = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    MAP[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    MAP[a][b] = min(MAP[a][b], c)

for mid in range(1, N + 1):
    for start in range(1, N + 1):
        if mid == start: continue
        for end in range(1, N + 1):
            if mid == end: continue
            if MAP[start][mid] == float('inf') or MAP[mid][end] == float('inf'):
                continue
            original = MAP[start][end]
            new = MAP[start][mid] + MAP[mid][end]
            MAP[start][end] = min(original, new)

for y in range(1, N + 1):
    for x in range(1, N + 1):
        if MAP[y][x] == float('inf'):
            print(0, end=" ")
        else:
            print(MAP[y][x], end=" ")
    print()