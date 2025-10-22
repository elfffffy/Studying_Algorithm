"""
소금과 후추
"""
M, N, K, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
B = [[0] * (N - W + 1) for _ in range(M - W + 1)]

for y in range(M - W + 1):
    for x in range(N - W + 1):
        arr = []
        for iy in range(y, y + W):
            for ix in range(x, x + W):
                arr.append(A[iy][ix])
        arr.sort()
        mid = arr[len(arr) // 2]
        B[y][x] = mid

for b in B:
    print(*b)