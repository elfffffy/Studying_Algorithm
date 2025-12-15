"""
배틀로얄
"""
import sys

input = sys.stdin.readline

X, Y, M = map(int, input().split())
enemies = [(int(input()), idx + 1) for idx in range(X)]
treatments = [(int(input()), idx + 1) for idx in range(Y)]

enemies.sort(reverse=True)
treatments.sort(reverse=True)

e_idx, t_idx = 0, 0
actions = X + Y
path = []
impossible = False

while actions > 0:
    if e_idx < X and enemies[e_idx][0] < M:
        M -= enemies[e_idx][0]
        path.append(-enemies[e_idx][1])
        actions -= 1
        e_idx += 1

    elif t_idx < Y:
        M += treatments[t_idx][0]
        path.append(treatments[t_idx][1])
        actions -= 1
        t_idx += 1

    else:
        print(0)
        impossible = True
        break

if not impossible:
    print(*path, sep="\n")
