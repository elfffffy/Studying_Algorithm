"""
도시 분할 계획
"""
import sys
input = sys.stdin.readline


def Find(x):
    if x == boss[x]:
        return x

    boss[x] = Find(boss[x])
    return boss[x]


def Union(t1, t2):
    global result
    a = Find(t1)
    b = Find(t2)

    if a == b:
        return

    boss[b] = a
    return


N, M = map(int, input().split())

edges = []
for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((weight, start, end))

edges.sort()

boss = [x for x in range(N + 1)]
result = 0
cnt = 0
max_v = 0

for w, s, e in edges:
    if Find(s) != Find(e):
        max_v = max(max_v, w)
        Union(s, e)
        result += w
        cnt += 1

        if cnt == N - 1:
            break

print(result - max_v)