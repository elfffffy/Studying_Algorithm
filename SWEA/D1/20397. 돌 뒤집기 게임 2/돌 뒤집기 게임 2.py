T = int(input())

for tc in range(1, T + 1):
    # N : 돌의 수
    # M : 뒤집기 횟수
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for m in range(M):
        # i번째 돌, 마주 보는 j개의 돌
        i, j = map(int, input().split())
        i = i - 1  # 인덱스 시작이 1
        mid = stones[i]

        # j개 만큼 뒤집을 수 있도록 함
        for distance in range(1, j + 1):
            left_ni = i + (-1 * distance)
            right_ni = i + (1 * distance)

            # 범위를 벗어날 때 break
            if left_ni < 0 or right_ni >= N: break

            # 범위를 벗어나지 않을 때 실행
            if stones[right_ni] == stones[left_ni]:
                if stones[right_ni] == 1 : stones[left_ni], stones[right_ni] = 0, 0
                else : stones[left_ni], stones[right_ni] = 1, 1

    print(f'#{tc}', *stones)
