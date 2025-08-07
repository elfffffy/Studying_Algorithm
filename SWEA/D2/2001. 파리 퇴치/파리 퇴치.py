T = int(input())


def catch_fly(y, x):
    sum_v = 0

    for i in range(M):
        for j in range(M):
            if y + i >= N or x + j >= N: continue
            sum_v += arr[y + i][x + j]

    return sum_v


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for y in range(N):
        for x in range(N):
            result = catch_fly(y, x)
            max_v = max(max_v, result)

    print(f'#{tc} {max_v}')
