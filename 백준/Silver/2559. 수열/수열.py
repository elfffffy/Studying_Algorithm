"""
백준 - 수열
"""

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

sum_v = sum(numbers[:K])
max_v = sum_v

for i in range(N - K):
    sum_v -= numbers[i]
    sum_v += numbers[i + K]

    if max_v < sum_v:
        max_v = sum_v

print(max_v)