T = int(input())


def catch(y, x):
    cnt = 0

    for i in range(M):
        for j in range(M):
            ny = y + i
            nx = x + j
            if ny >= N or nx >= N: continue
            if arr[ny][nx] == '@':
                cnt += 1

    return cnt


for tc in range(1, T + 1):
    # N: 두더지의 집 크기
    # M : 망치 크기
    N, M = map(int, input().split())

    # _ 빈칸, @ 두더지
    arr = [list(input()) for _ in range(N)]

    max_v = 0

    # y = 0, 1, 2
    # x = 0, 1, 2
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            result = catch(y, x)

            # 두더지를 잡을 수 있는 최대 수
            max_v = max(max_v, result)

    print(f'#{tc} {max_v}')
