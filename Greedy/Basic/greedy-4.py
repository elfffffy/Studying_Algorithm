n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어떨어지는 수)가 될 떄까지 1을 한 번에 빼기
    target = (n // k) * k
    result += (n - target)
    n = target  # 이떄, n은 k의 배수가 된다.

    # n이 k보다 작을 때
    if n < k:
        break

    # k로 나누기
    n //= k
    result += 1

# 마지막 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
