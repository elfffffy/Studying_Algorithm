T = int(input())

for tc in range(1, T + 1):
    # N: 크기
    # M: 회문의 길이
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = False

    for y in range(N):
        if result:
            break
        for i in range(N - M + 1):
            text = ""
            for x in range(i, M + i):
                text += arr[y][x]

            if text == text[::-1]:
                print(f'#{tc} {text}')
                result = True

            if result:
                break

    for x in range(N):
        if result:
            break
        for i in range(N - M + 1):
            text = ""
            for y in range(i, i + M):
                text += arr[y][x]

            if text == text[::-1]:
                print(f'#{tc} {text}')
                result = True

            if result:
                break
