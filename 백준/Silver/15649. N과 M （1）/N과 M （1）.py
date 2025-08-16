n, m = map(int, input().split())


def func(lev):
    if lev == m:
        print(*path)
        return

    for i in range(1, n + 1):
        if used[i] != 0 :
            continue
        path.append(i)
        used[i] = 1
        func(lev + 1)
        path.pop()
        used[i] = 0


path = []
used = [0] * (n + 1)
func(0)