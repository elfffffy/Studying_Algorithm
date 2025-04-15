n, m = map(int, input().split())
# 0:북/1:동/2:남/3:서
row, column, head = map(int, input().split())
# 0:육지/1:바다
land = []
for i in range(n):
    land.append(list(map(int, input().split())))

ahead = [(-1, 0), (0, 1), (1, 0), (0, -1)]
routes = [(0, 3, 2, 1, 0), (1, 0, 3, 2, 1), (2, 1, 0, 3, 2), (3, 2, 1, 0, 3)]
record = [(row, column)]

result = 0

while True:
    moved = False
    route = routes[head]
    for i in route[1:]:
        new_row = row + ahead[i][0]
        new_column = column + ahead[i][1]
        if land[new_row][new_column] == 1:
            continue
        else:
            if (new_row, new_column) in record:
                continue
            head = i
            row, column = new_row, new_column
            record.append((row, column))
            result += 1
            moved = True
            break
    if not moved:
        new_row = row + ahead[route[2]][0]
        new_column = column + ahead[route[2]][1]
        if land[new_row][new_column] == 1:
            break
        else :
            row, column = new_row, new_column
            record.append((row, column))
            result += 1

print(result)
