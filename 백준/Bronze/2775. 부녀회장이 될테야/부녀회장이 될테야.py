T = int(input())

for tc in range(1, T + 1):
    # k층에 n호에는 몇 명이 살고 있나요?
    k = int(input())
    n = int(input())

    apt = [[0] * 15 for _ in range(15)]

    for x in range(1, 15):
        apt[0][x] = x

    for y in range(15):
        apt[y][1] = 1

    for y in range(1, 15):
        for x in range(2, 15):
            apt[y][x] = apt[y][x - 1] + apt[y - 1][x]

    print(apt[k][n])