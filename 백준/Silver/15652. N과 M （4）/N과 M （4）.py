n, m = map(int, input().split())


def func(lev, start):
    if lev == m:
        print(*path)
        return
    else:
        for i in range(start, n + 1):
            path.append(i)
            func(lev + 1, i)
            path.pop()


path = []
func(0, 1)