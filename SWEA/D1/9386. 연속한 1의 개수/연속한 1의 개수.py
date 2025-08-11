T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = input()

    cnt = 0
    max_v = 0

    for num in nums:
        if num == '1':
            cnt += 1
            max_v = max(cnt, max_v)
        else:
            cnt = 0

    print(f'#{tc} {max_v}')
