"""

"""
T = int(input())


def catch(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sum_v = arr[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or nx >= N or ny >= N: continue

        if arr[y][x] <= arr[ny][nx]:
            break

        sum_v += arr[ny][nx]
    return sum_v


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = float('-inf')
    for y in range(N):
        for x in range(N):
            result = catch(y, x)
            if result > max_v:
                max_v = result

    print(f'#{tc} {max_v}')
