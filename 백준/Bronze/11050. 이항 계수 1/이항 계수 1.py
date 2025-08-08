"""
5 * 4 // 2 * 1 = 10
"""
N, M = map(int, input().split())

top_v = 1
for i in range(N, N - M, -1):
    top_v *= i

bottom_v = 1
for j in range(M, 0, -1):
    bottom_v *= j

print(top_v // bottom_v)
