"""
네트워크 연결
"""
import sys

input = sys.stdin.readline


def Find(x):
    if boss[x] == x:
        return x
    boss[x] = Find(boss[x])
    return boss[x]


def Union(a, b):
    t1 = Find(a)
    t2 = Find(b)

    if t1 == t2: return
    boss[t2] = t1


N = int(input())
M = int(input())
connections = [list(map(int, input().split())) for _ in range(M)]

# 비용을 기준으로 정렬
# (a 컴퓨터, b 컴퓨터, 연결 비용)
connections.sort(key=lambda x: x[-1])

# Union-Find
total_cost = 0
cnt = 0
boss = [x for x in range(N + 1)]
for a, b, c in connections:
    if Find(a) == Find(b): continue
    Union(a, b)
    total_cost += c
    cnt += 1

    if cnt == N - 1:
        break

print(total_cost)