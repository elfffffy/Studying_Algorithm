import heapq


def bfs(y, x):
    global rupee

    # 우선순위 큐 생성
    pq = []

    # 시작점 추가하기 (현재 비용, 좌표(y,x))
    heapq.heappush(pq, (cave[y][x], (y, x)))

    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 탐색 시작
    while pq:

        # pq에서 꺼내기 = 현재 비용이 가장 작은 위치 꺼내기
        minus, spot = heapq.heappop(pq)

        # 이미 더 적은 비용으로 방문한 기록이 있으면 continue
        # 탐색을 시작하기 위해 가져온 비용이 원래 기록된 것 보다 크다면,
        # 탐색할 필요가 없다.
        if rupee[spot[0]][spot[1]] < minus:
            continue

        # 도착지점이면 종료
        if spot == (N - 1, N - 1):
            return minus

        # 인접한 네 방향 탐색
        for i in range(4):
            ny, nx = spot[0] + dy[i], spot[1] + dx[i]

            # 범위를 벗어나면 무시
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

            # (현재 위치까지 비용 + 다음 칸 비용)이 
            # 기존 비용(rupee에 기록된 값)보다 작다면 변경
            if rupee[ny][nx] > minus + cave[ny][nx]:
                rupee[ny][nx] = minus + cave[ny][nx]

                # 새롭게 업데이트 된 위치와 비용 정보를 큐에 추가
                heapq.heappush(pq, (rupee[ny][nx], (ny, nx)))


# 테스트 케이스 번호 시작은 1
tc = 1

while True:

    # 동굴의 크기
    N = int(input())

    # 0을 입력 받으면 종료
    if N == 0:
        break

    # 동굴 정보
    # 해당 위치를 지날 때 감소되는 루피의 양을 나타낸다.
    cave = [list(map(int, input().split())) for _ in range(N)]

    # 각 칸까지 최소 비용을 기록할 리스트
    # 최소 비용을 구해야하므로, 무한히 큰 값으로 초기화
    rupee = [[float('inf')] * N for _ in range(N)]

    # 결과 출력
    print(f'Problem {tc}: {bfs(0, 0)}')

    # 테스트 케이스 번호 증가
    tc += 1
