n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

# 보드 생성
board = [[0] * (n + 1) for _ in range (n + 1)]
# 방향 회전 정보 리스트
info = []

# 사과의 개수 만큼 사과의 자표 입력 받고 보드에 적용하기
for _ in range (k) :
    a, b = map(int, input().split())
    board[a][b] = 1
    
# 방향 회전 정보 입력 받기
l = int(input())
for _ in range (l) :
    sec, direct = input().split()
    info.append((int(sec), direct)) # 튜플 형식으로 저장

# 방향에 대한 정보 (RDLU) 
moveX = [0, 1, 0, -1] # 행 변화
moveY = [1, 0, -1, 0] # 열 변화

def turn(direction, info_direction) :
    if info_direction == "D" :
        direction = (direction + 1) % 4
    else :
        direction = (direction - 1) % 4
    return direction

def simulate() :
    x, y = 1, 1
    board[x][y] = 2 # 뱀이 위치하는 곳은 2로 표시
    direction = 0
    time = 0
    rotation = 0 # 다음에 회전할 정보
    snake = [(x, y)] # 뱀이 차지하고 있는 위치 정보

    while True :
        nx = x + moveX[direction] # 다음 위치
        ny = y + moveY[direction] # 다음 위치

        # 맵 범위 안에 있으며서 뱀의 몸통이 없을 경우
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2 :
            # 사과가 없는 경우
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                snake.append((nx,ny))
                px, py = snake.pop(0) # 이전 위치
                board[px][py] = 0

            # 사과가 있는 경우
            if board[nx][ny] == 1 :
                board[nx][ny] = 2
                snake.append((nx, ny))
        # 벽이나 몸통에 부딪힐 경우
        else :
            time += 1
            break

        x, y = nx, ny
        time += 1

        # 회전
        if rotation < l and time == info[rotation][0] :
            direction = turn(direction, info[rotation][1])
            rotation += 1

    return time

print(simulate())