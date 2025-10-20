"""
백준 - 플로이드
"""
import sys

input = sys.stdin.readline


def print_func(N, MAP):
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if MAP[y][x] == float('inf'):
                print(0, end=" ")
            else:
                print(MAP[y][x], end=" ")
        print()


def solve():
    N = int(input())
    M = int(input())
    INF = float('inf')
    MAP = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        MAP[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        if MAP[a][b] > c:
            MAP[a][b] = c

    for mid in range(1, N + 1):
        for start in range(1, N + 1):
            for end in range(1, N + 1):
                if MAP[start][end] > MAP[start][mid] + MAP[mid][end]:
                    MAP[start][end] = MAP[start][mid] + MAP[mid][end]

    print_func(N, MAP)


solve()