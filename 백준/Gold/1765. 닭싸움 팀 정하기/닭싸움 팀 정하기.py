"""
❌ 틀렸습니다! 몬데!! GG
백준 - 닭싸움 팀 정하기
"""


def Find(x):
    if x == boss[x]:
        return x

    boss[x] = Find(boss[x])
    return boss[x]


def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)

    if a == b: return
    boss[b] = a


n = int(input())
m = int(input())
boss = [x for x in range(n + 1)]
enemy = [[] for _ in range(n + 1)]

for _ in range(m):
    t, p, q = input().split()
    p, q = int(p), int(q)
    if t == 'F':
        Union(p, q)
    else:
        enemy[p].append(q)
        enemy[q].append(p)

# boss [0, 1, 2, 3, 4, 3, 4]
# enemy [[], [4, 2], [], [], [], [], []]

for i in range(1, n + 1):
    if len(enemy[i]) < 2 : continue
    for j in range(len(enemy[i]) - 1):
        Union(enemy[i][j], enemy[i][j + 1])

for i in range(len(boss)):
    Find(i)
# boss [0, 1, 4, 3, 4, 3, 4]

print(len(set(boss)) - 1)
