T = int(input())


def water_shoot(y, x):
    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sum_v = arr[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 물풍선 모양 '+' 안되면 break
        if ny < 0 or nx < 0 or ny >= N or nx >= N: return 0

        # 값 비교
        if arr[y][x] <= arr[ny][nx]:
            return 0
        else:
            sum_v += arr[ny][nx]


    # 모든 조건을 충족 했을 경우
    else:
        return sum_v


for tc in range(1, T + 1):
    # 맵의 크기
    N = int(input())

    # 맵의 점수
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for y in range(N):
        for x in range(N):
            result = water_shoot(y, x)

            # 물풍선 값 중 제일 큰 값
            max_v = max(max_v, result)

    print(f'#{tc} {max_v}')
