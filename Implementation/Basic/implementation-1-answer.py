n = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 하나씩 이동 확인
for plan in plans :
    # 이동 후 좌표 확인
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어난 경우
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    x, y = nx , ny

print(x, y)
