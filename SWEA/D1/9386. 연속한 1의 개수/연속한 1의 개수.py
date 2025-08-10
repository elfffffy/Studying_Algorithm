T = int(input())

for tc in range(1, T + 1):
    # 수열의 길이
    N = int(input())

    # 0과 1로 구성된 수열
    num = input()

    cnt = 0
    max_v = float('-inf')

    for x in num:
        # 0일 때 실행
        if x == '0':
            # 지금까지의 연속된 1의 개수와 최댓값 비교 후 갱신
            max_v = max(cnt, max_v)
            cnt = 0
            continue

        # 1일 때 실행
        else:
            cnt += 1

    # 수열이 1로 끝나는 경우를 대비해 최종 갱신
    max_v = max(cnt, max_v)

    print(f'#{tc} {max_v}')
