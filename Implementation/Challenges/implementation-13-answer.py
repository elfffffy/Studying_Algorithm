from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    # 맵 정보 한 줄 씩 입력 받고, 바로 필요한 데이터 정리하기
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))  # 집
        elif data[c] == 2:
            chicken.append((r, c))  # 차킨집

# 치킨집 후보 => 조합 이용하기
candidates = list(combinations(chicken, m))


# 치킨 거리의 합 계산
def get_sum(candidate):
    result = 0
    # 각 집에 대해서
    for hx, hy in house:
        temp = 1e9
        # 가까운 치킨집 찾기
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

# 치킨 거리의 합의 최소 찾기
result = 1e9
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)
