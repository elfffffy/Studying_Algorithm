from itertools import combinations

n, m = map(int, (input().split()))
cities = []

for _ in range(n):
    city = list(map(int, input().split()))
    cities.append(city)

chicken = []
house = []
distances = []

for i in range(len(cities)):
    for j in range(len(cities[i])):
        if cities[i][j] == 1:
            house.append([i, j])

        if cities[i][j] == 2:
            chicken.append([i, j])

chicken = list(combinations(chicken, m))
distance = 0
sum_distance = 0
result = 0

for i in chicken :
    sum_distance = 0
    for j in house :
        distance = 0
        for k in range(m) :
            if distance == 0:
                distance = abs(i[k][0] - j[0]) + abs(i[k][1] - j[1])
            else:
                distance = min(distance, abs(i[k][0] - j[0]) + abs(i[k][1] - j[1]))

        sum_distance += distance
    if result == 0 :
        result = sum_distance
    else :
        result = min(sum_distance, result)

print(result)
