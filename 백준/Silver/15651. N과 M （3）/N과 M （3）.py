n, m = map(int, input().split())


def func(lev):
    if lev == m:
        print(*path)
        return
    else:
        for i in range(1, n + 1):
            path.append(i)
            func(lev + 1)
            path.pop()


path = []
func(0)