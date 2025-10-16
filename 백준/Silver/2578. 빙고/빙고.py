"""
백준 - 빙고
"""


def garo():
    cnt = 0
    for i in range(5):
        if sum(board[i]) == -5:
            cnt += 1
    return cnt


def sero():
    cnt = 0
    for x in range(5):
        sum_v = 0
        for y in range(5):
            if board[y][x] == -1:
                sum_v -= 1
        if sum_v == -5:
            cnt += 1
    return cnt


def daegag1():
    pos = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    sum_v = 0
    for y, x in pos:
        if board[y][x] == -1:
            sum_v -= 1
    if sum_v == -5:
        return 1
    return 0


def daegag2():
    pos = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]
    sum_v = 0
    for y, x in pos:
        if board[y][x] == -1:
            sum_v -= 1
    if sum_v == -5:
        return 1
    return 0


board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]


def find_target_pos(target):
    for y in range(5):
        for x in range(5):
            if board[y][x] == target:
                return y, x


bingo = False
answer = 0
for i in range(5):
    for j in range(5):
        target = call[i][j]
        y, x = find_target_pos(target)
        board[y][x] = -1
        answer += 1
        cnt = 0
        cnt += garo()
        cnt += sero()
        cnt += daegag1()
        cnt += daegag2()
        if cnt >= 3:
            bingo = True
            break
    if bingo:
        break

print(answer)