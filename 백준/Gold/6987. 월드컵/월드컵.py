"""
백준 - 월드컵
"""
import itertools


def battle(lev):
    global result

    if lev == len(teams):
        for r in result:
            if r[0] != 0 or r[1] != 0 or r[2] != 0:
                return False
        return True

    a, b = teams[lev]
    a_win = result[a][0]
    a_draw = result[a][1]
    a_lose = result[a][2]
    b_win = result[b][0]
    b_draw = result[b][1]
    b_lose = result[b][2]

    if a_win > 0 and b_lose > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        if battle(lev + 1): return True
        result[a][0] += 1
        result[b][2] += 1

    if a_draw > 0 and b_draw > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        if battle(lev + 1): return True
        result[a][1] += 1
        result[b][1] += 1

    if a_lose > 0 and b_win > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        if battle(lev + 1): return True
        result[a][2] += 1
        result[b][0] += 1


for tc in range(4):
    result = []
    data = list(map(int, input().split()))
    for i in range(6):
        result.append([data[i * 3], data[i * 3 + 1], data[i * 3 + 2]])

    teams = list(itertools.combinations([x for x in range(6)], 2))
    if battle(0):
        print(1)
    else:
        print(0)