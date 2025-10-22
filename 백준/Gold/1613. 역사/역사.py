"""
백준 - 역사
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
accidents = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    first, second = map(int, input().split())
    accidents[first][second] = 1

for mid in range(1, N + 1):
    for start in range(1, N + 1):
        if accidents[start][mid] == 0: continue
        for end in range(1, N + 1):
            if accidents[mid][end] == 0: continue
            accidents[start][end] = 1

S = int(input())
for _ in range(S):
    first, second = map(int, input().split())
    if accidents[first][second] == 1:
        print(-1)
    elif accidents[second][first] == 1:
        print(1)
    else:
        print(0)