dwarfs = [int(input()) for _ in range(9)]
answer = []


def func(lev, start):
    global answer

    if lev == 7:
        if sum(path) == 100:
            answer = sorted(path)
            return
    else:
        for i in range(start, 9):
            path.append(dwarfs[i])
            func(lev + 1, i + 1)
            path.pop()


path = []
func(0, 0)
print(*answer, sep="\n")