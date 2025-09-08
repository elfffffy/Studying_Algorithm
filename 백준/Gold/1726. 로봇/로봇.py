# ❌ 실패... What's the problem...❌
from collections import deque

# 동 서 남 북 = 우 좌 하 상
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


# 현재 바라보고 있는 방향에서 좌회전, 우회전 했을 때
# 갈 수 있는 방향을 리턴한다.
# 0: 동, 1: 서, 2: 남, 3: 북
def rotating(direction):
    # r_direction = [left, right]
    if direction == 0:
        r_direction = [2, 3]
    elif direction == 1:
        r_direction = [3, 2]
    elif direction == 2:
        r_direction = [1, 0]
    else:
        r_direction = [0, 1]

    return r_direction


def bfs(y, x, s_dir):
    global ey, ex, e_dir

    # 방문 체크 배열 + 방향 정보 [행][열][방향]
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    # 큐 생성
    # 큐에 담기는 정보 : (현재 y, 현재 x, 현재 방향, 회전 횟수, 직진 횟수)
    q = deque()
    q.append((y, x, s_dir, 0, 0))
    visited[y][x][s_dir] = True

    while q:
        cy, cx, c_dir, rotate_cnt, straight_cnt = q.popleft()

        # 도착 지점에 도달했을 때 실행
        if cy == ey - 1 and cx == ex - 1 and c_dir == e_dir - 1:
            return straight_cnt + rotate_cnt

            # # 방향이 일치할 때
            # if c_dir == e_dir - 1:
            #     return straight_cnt + rotate_cnt
            #
            # # 방향일 일치하지 않으면 회전 + 1
            # else:
            #     return straight_cnt + rotate_cnt + 1

        # 직진
        # 직진(i)은 최대 3까지 가능하다.
        for i in range(1, 4):
            ny = cy + dy[c_dir] * i
            nx = cx + dx[c_dir] * i

            # 범위를 벗어나거나 벽을 만나면 더 이상 직진 x
            if (ny < 0 or nx < 0 or ny >= n or nx >= m) or arr[ny][nx] == 1: break

            # 같은 방향으로 이미 방문했으면 continue
            if visited[ny][nx][c_dir]: continue

            # 다음 직진 정보를 큐에 삽입
            q.append((ny, nx, c_dir, rotate_cnt, straight_cnt + 1))

            # 방문 처리
            visited[ny][nx][c_dir] = True

        # 회전
        # 좌회전, 우회전 => 2번
        for i in range(2):

            # 회전 가능한 방향 리스트
            # c_dir = 1 -->  d_list = [3, 2]
            d_lst = rotating(c_dir)

            # 같은 방향으로 이미 방문했다면 continue
            if visited[cy][cx][d_lst[i]]: continue

            # 회전만 할 경우, 좌표는 달라지지 않기 때문에
            # 좌표는 같고, 새로운 방향 정보와 회전 정보를 업데이트 하여
            # 큐에 삽입한다.
            q.append((cy, cx, d_lst[i], rotate_cnt + 1, straight_cnt))

            # 방문 처리
            visited[cy][cx][d_lst[i]] = True


n, m = map(int, input().split())

# 0: 가능, 1: 불가능
arr = [list(map(int, input().split())) for _ in range(n)]

# 출발 지점 (행, 열, 방향)
sy, sx, s_dir = map(int, input().split())

# 도착 지점 (행, 열, 방향)
ey, ex, e_dir = map(int, input().split())

print(bfs(sy - 1, sx - 1, s_dir - 1))
