T = int(input())


def move(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0

    for i in range(4):
        r = 1
        while True:
            ny = y + dy[i] * r
            nx = x + dx[i] * r
            if ny < 0 or nx < 0 or ny >= N or nx >= N: break
            if arr[ny][nx] == 0:
                cnt += 1
                r += 1
            else:
                break

    return cnt


for tc in range(1, T + 1):
    N = int(input())

    # 빈칸 0 벽 1 괴물 2
    arr = [list(map(int, input().split())) for _ in range(N)]

    wall = 0
    light = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                wall += 1
            if arr[y][x] == 2:
                light = move(y, x)

    print(f'#{tc} {N * N - wall - light - 1}')
