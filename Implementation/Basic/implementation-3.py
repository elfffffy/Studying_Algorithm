start = input()
data = []

for i in range(len(start)):
    data.append(start[i])

value = {'a': 1,
         'b': 2,
         'c': 3,
         'd': 4,
         'e': 5,
         'f': 6,
         'g': 7,
         'h': 8,
         }

move_types = ['RRU', 'RRD', 'LLU', 'LLD', 'DDR', 'DDL', 'UUR', 'UUL']
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0

for move_type in move_types:
    x, y = value[data[0]], int(data[1])
    for move in move_type:
        for i in range(len(direction)):
            if move == direction[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                x = nx
                y = ny

    if nx <= 0 or ny <= 0:
        continue
    else:
        result += 1

print(result)
