t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    ans = 'NO'
    max_v = 0

    # 행순회
    for y in range(n):
        cnt = 0
        for x in range(n):
            if arr[y][x] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    ans = 'YES'
                    max_v = max(cnt, max_v)
                cnt = 0

            if cnt >= 5:
                max_v = max(cnt, max_v)
                ans = 'YES'

    if ans == 'NO':
        # 열순회
        for x in range(n):
            cnt = 0
            for y in range(n):
                if arr[y][x] == 'o':
                    cnt += 1
                else:
                    if cnt >= 5:
                        ans = 'YES'
                        max_v = max(cnt, max_v)
                    cnt = 0

                if cnt >= 5:
                    max_v = max(cnt, max_v)
                    ans = 'YES'

    if ans == 'NO':
        # 대각선 좌 -> 우
        for y in range(n):
            for x in range(n):
                if arr[y][x] == 'o':
                    i = 0
                    cnt = 0
                    while y + i < n and x + i < n:
                        if arr[y + i][x + i] == 'o':
                            cnt += 1
                        else:
                            if cnt >= 5:
                                max_v = max(cnt, max_v)
                                ans = 'YES'
                            cnt = 0
                        i += 1
                    if cnt >= 5:
                        max_v = max(cnt, max_v)
                        ans = 'YES'

    if ans == 'NO':
        # 대각선 우 -> 자
        for y in range(n):
            for x in range(n - 1, -1, -1):
                if arr[y][x] == 'o':
                    i = 0
                    cnt = 0
                    while y + i < n and x - i >= 0:
                        if arr[y + i][x - i] == 'o':
                            cnt += 1
                        else:
                            if cnt >= 5:
                                max_v = max(cnt, max_v)
                                ans = 'YES'
                            cnt = 0
                        i += 1
                    if cnt >= 5:
                        max_v = max(cnt, max_v)
                        ans = 'YES'

    print(f'#{tc} {ans}')
