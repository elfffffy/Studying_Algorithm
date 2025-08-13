T = int(input())

for tc in range(1, T + 1):
    # 칠할 영역의 개수
    N = int(input())

    # r1, c1: 왼쪽 위 모서리
    # r2, c2: 오른쪽 아래 모서리
    # 빨강:1 파랑 2
    info = [list(map(int, input().split())) for _ in range(N)]

    arr = [[0] * 10 for _ in range(10)]

    for i in info:
        for y in range(i[0], i[2] + 1):
            for x in range(i[1], i[3] + 1):
                arr[y][x] += i[4]

    cnt = 0
    for col in arr:
        cnt += col.count(3)

    print(f'#{tc} {cnt}')