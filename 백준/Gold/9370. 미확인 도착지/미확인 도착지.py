"""
백준 - 미확인 도착지
계속 16%에서 "틀렸습니다" 떠서 GPT 도움 받았습니다...

1. 최단 거리 구하기 => 다익스트라
2. G-H를 지나면서 최단 경로로 도달 가능한 목적지들을 구하기 = 최단거리가 G-H를 지나는 길이어야 한다!!!
    - G-H를 지나서 목적지에 도달하는 최단 거리
    - G-H를 지나지 않고 목적지에 도달하는 최단 거리
    - G-H 지나는 거리 = 최단 거리

<HELP!!! GPT!!!>
float('inf") 조건 검사
- inf == inf 도 True이기 때문에 도달 불가능한 경우도 정답 후보에 들어가게 된다.
- 따로 조건을 추가해서 빼줘야 한다.

"""
import heapq


# 최단 거리 계산
def bfs(start):
    pq = []
    heapq.heappush(pq, (0, start, 0))  # (거리, 현재 노드, G-H 통과 여부)

    # 최단 거리 저장 리스트
    # best[node][0] = 통과 x 했을 때의 최단 거리
    # best[node][1] = 통과 o 했을 떄의 최단 거리
    best = [[float('inf')] * 2 for _ in range(N + 1)]
    best[start][0] = 0

    while pq:
        c_dist, c_node, passed = heapq.heappop(pq)

        # 이미 더 짧은 경로가 저장되어 있다면, 더 볼 필요 없다.
        if best[c_node][passed] < c_dist: continue

        # 인접 노드 탐색
        for n_dist, n_node in graph[c_node]:

            # passed == 1 : G-H를 지났다. => n_passed = 1 (유지)
            # 현재 이동이 G-H 이다. => n_passed = 1로 변경
            if passed or (c_node, n_node) == (G, H) or (c_node, n_node) == (H, G):
                n_passed = 1

            # 위의 경우가 아니면 0
            else:
                n_passed = 0

            # 새로운 경로가 기존 경로보다 짧으면 갱신
            if best[n_node][n_passed] > n_dist + c_dist:
                best[n_node][n_passed] = n_dist + c_dist

                # 새로운 상태의 값들을 추가해서 탐색할 수 있도록 한다.
                heapq.heappush(pq, (c_dist + n_dist, n_node, n_passed))

    return best


Test = int(input())

for tc in range(1, Test + 1):
    N, M, T = map(int, input().split())  # n 교차로, m 도로, 목적지 t
    S, G, H = map(int, input().split())  # s 출발지, g -- h

    # 도로 정보 - 인접 리스트
    # graph[node1] = [(거리, node2), ...]
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    # 목적지 후보 입력
    destination = []
    for _ in range(T):
        destination.append(int(input()))

    # S에서 출발하여 모든 노드까지의 최단 거리 계산
    possible_destinations = bfs(S)

    # 오름차순 정렬 => sorted(destination)
    for d in sorted(destination):
        if (possible_destinations[d][1] <= possible_destinations[d][0]) and possible_destinations[d][1] != float('inf'):
            print(d, end=" ")
    print()
