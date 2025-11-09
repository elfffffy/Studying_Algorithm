"""
치킨 배달
"""


def calculate(house, case):
    min_v = float('inf')
    for chicken_pos in case:
        dist = abs(chicken_pos[0] - house[0]) + abs(chicken_pos[1] - house[1])
        min_v = min(min_v, dist)

    return min_v


from itertools import combinations

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]  # 0 빈 칸, 1 집, 2 치킨 집

chicken = []
houses = []

for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            chicken.append((y, x))
        elif MAP[y][x] == 1:
            houses.append((y, x))

total_min_v = float('inf')
for case in combinations(chicken, M):
    sum_v = 0
    for house in houses:
        result = calculate(house, case)
        sum_v += result
        if sum_v > total_min_v:
            break
    else:
        total_min_v = min(total_min_v, sum_v)

print(total_min_v)