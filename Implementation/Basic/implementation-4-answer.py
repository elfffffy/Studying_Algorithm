# 0:육지/1:바다
# 0:북/1:동/2:남/3:서

# 세로 n, 가로 m
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성
# 기본은 0이고, 방문했을 때 1로 변경할 것
d = [[0] * m for _ in range (n)]

# 현재 캐릭터 정보 입력 받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 => direction 정하기
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3
        
# 시뮬레이션
count = 1
turn_time = 0
while True :
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 바다로 막혀있는 경우
        else :
            break
        turn_time = 0

print(count)
