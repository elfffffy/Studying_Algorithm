"""
백준 - 두 수의 합
"""
N = int(input())
numbers = list(map(int, input().split()))
target = int(input())
numbers.sort()
cnt = 0
left, right = 0, N - 1
while left != right:
    sum_v = numbers[left] + numbers[right]
    if sum_v > target:
        right -= 1
    elif sum_v < target:
        left += 1
    else:
        cnt += 1
        left += 1

print(cnt)