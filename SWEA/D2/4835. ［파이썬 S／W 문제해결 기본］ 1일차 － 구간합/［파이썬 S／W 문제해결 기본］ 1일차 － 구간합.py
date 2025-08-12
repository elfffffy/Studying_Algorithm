T = int(input())

for tc in range(1, T + 1):
    # N : n개의 정수
    # M : 이웃 범위
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = float('-inf')
    min_v = float('inf')

    for i in range(N - M + 1):
        sum_v = 0
        for j in range(M):
            sum_v += arr[i + j]
        max_v = max(sum_v, max_v)
        min_v = min(sum_v, min_v)

    print(f'#{tc} {max_v - min_v}')