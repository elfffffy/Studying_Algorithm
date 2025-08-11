T = int(input())

for tc in range(1, T + 1):
    # 퍼즐 가로 세로 N
    # 단어의 길이 K
    N, K = map(int, input().split())

    # 흰색 1. 검은색 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 행
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

        if cnt == K:
            result += 1

    # 열
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{tc} {result}')
