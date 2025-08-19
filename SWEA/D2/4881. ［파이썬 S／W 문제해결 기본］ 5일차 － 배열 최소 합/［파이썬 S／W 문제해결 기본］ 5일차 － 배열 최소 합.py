T = int(input())


def func(lev, sum_v):
    global min_v

    if sum_v >= min_v:
        return

    if lev == n:
        min_v = min(min_v, sum_v)
        return

    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            func(lev + 1, sum_v + arr[lev][i])
            used[i] = 0


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n
    min_v = float('inf')
    func(0, 0)

    print(f'#{tc} {min_v}')