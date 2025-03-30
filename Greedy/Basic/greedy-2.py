n, m, k = map(int, input().split())
numberList = list(map(int, input().split()))

numberList.sort()
first = numberList[n - 1]
second = numberList[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0

result += count * first
result += (m-count) * second

print(result)




