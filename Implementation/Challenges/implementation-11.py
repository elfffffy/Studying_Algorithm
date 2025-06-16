n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

# 보드 생성
board = [[0] * n for _ in range(n)]

# 사과의 개수 만큼 사과의 자표 입력 받고 보드에 적용하기
for i in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

l = int(input())  # 뱡향 전환 횟수

# 방향 전환 횟수 만큼 (실행 시간 + 방향) 입력 받기
sec_list = []  # 입력 받은 실행 시간
direct_list = []  # 입력 받은 방향

for i in range(l):
    sec, direct = input().split()
    sec_list.append(int(sec))
    direct_list.append(direct)

# 실행
current_y = 0
current_x = 0
current_time = 0
current_direction = 0
snake = [[0, 0]]
# 방향에 대한 정보
moveX = [1, 0, -1, 0]  # RDLU
moveY = [0, 1, 0, -1]

while 0 <= current_x < n and 0 <= current_y < n:
    current_time += 1
    next_x = current_x + moveX[current_direction]
    next_y = current_y + moveY[current_direction]

    if next_x < 0 or next_x > n - 1 or next_y < 0 or next_y > n - 1:
        break
    if sec_list and current_time == sec_list[0]:
        if direct_list[0] == 'D':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4
        if [next_y, next_x] in snake:
            break
        snake.pop(0)
        snake.append([next_y, next_x])
        direct_list.pop(0)
        sec_list.pop(0)
    else:
        if [next_y, next_x] in snake:
            break
        else:
            if board[next_y][next_x] == 0:
                if snake:
                    snake.pop(0)
                    snake.append([next_y, next_x])
            else:
                if snake:
                    snake.append([next_y, next_x])
                else:
                    snake.append([current_y, current_x])
                    snake.append([next_y, next_x])
                board[next_y][next_x] = 0

    current_x = next_x
    current_y = next_y

print(current_time)