def is_in_garo(cy, tar):
    if tar in MAP[cy]:
        return True
    return False


def is_in_sero(cx, tar):
    for i in range(9):
        if MAP[i][cx] == tar:
            return True
    return False


def is_in_square(cy, cx, tar):
    if cy < 3:
        cy = 0
    elif cy >= 6:
        cy = 6
    else:
        cy = 3

    if cx < 3:
        cx = 0
    elif cx >= 6:
        cx = 6
    else:
        cx = 3

    for ny in range(cy, cy + 3):
        for nx in range(cx, cx + 3):
            if MAP[ny][nx] == tar:
                return True
    return False


def can_put(cy, cx, tar):
    if is_in_garo(cy, tar) or is_in_sero(cx, tar) or is_in_square(cy, cx, tar):
        return False
    return True


def func(idx):
    global flag

    if idx == len(empty):
        flag = True
        return

    cy, cx = empty[idx]
    for i in range(1, 10):
        if can_put(cy, cx, i):
            MAP[cy][cx] = i
            func(idx + 1)
            if flag: return
            MAP[cy][cx] = 0


MAP = [list(map(int, input().split())) for _ in range(9)]

empty = []
for y in range(9):
    for x in range(9):
        if MAP[y][x] == 0:
            empty.append((y, x))

flag = False
func(0)
for m in MAP:
    print(*m)
