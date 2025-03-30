n, m = map(int, input().split())
result = 0

# 한 줄씩 입력 받아 확인하기
for i in range (n) :
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 값 찾기
    min_value = 10001
    for j in data :
        min_value = min(min_value, j)
    # 작은 값 중에서 가장 큰 값 찾기
    result = max(min_value, result)

print(result)



