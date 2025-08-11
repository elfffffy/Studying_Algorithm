T = int(input())


def bomb(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sum_v = arr[y][x]

    for i in range(4):
        p = 1
        while True:
            ny = y + dy[i] * p
            nx = x + dx[i] * p

            if ny < 0 or nx < 0 or ny >= N or nx >= N: break
            sum_v += arr[ny][nx]
            p += 1

    return sum_v


for tc in range(1, T + 1):
    # N x N
    N = int(input())

    # 물풍선
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    max_v = 0
    for y in range(N):
        for x in range(N):
            result = bomb(y, x)
            max_v = max(result, max_v)

    print(f'#{tc} {max_v}')
