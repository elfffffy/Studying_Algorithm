T = int(input())

for tc in range(1, T + 1):
    # N : 전등의 개수
    N = int(input())

    # 조작 전 스위치 A, B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        # A와 B가 다른 지점이 발견된 경우
        if A[i] != B[i]:

            # 스위치 변경
            cnt += 1

            # 그 다른 지점에서 N까지 스위치 바꾸기
            for turn_off in range(i, N):
                A[turn_off] = 1 - A[turn_off]

    print(f'#{tc} {cnt}')
