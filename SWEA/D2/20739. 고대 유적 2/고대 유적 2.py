t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0

    # 행순회
    for y in range(n):
        cnt = 0
        for x in range(m):
            if arr[y][x] == 1:
                cnt += 1
            else:
                max_v = max(max_v, cnt)
                cnt = 0

        max_v = max(max_v, cnt)

    # 열순회
    for x in range(m):
        cnt = 0
        for y in range(n):
            if arr[y][x] == 1:
                cnt += 1
            else:
                max_v = max(max_v, cnt)
                cnt = 0

        max_v = max(max_v, cnt)

    if max_v == 1:
        max_v = 0
        
    print(f'#{tc} {max_v}')