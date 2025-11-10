"""
백준 - 미확인 도착지
"""
import heapq


def bfs(start):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    best = [[float('inf')] * 2 for _ in range(N + 1)]  # [[False, True], ...]
    best[start][0] = 0

    while pq:
        c_dist, c_node, passed = heapq.heappop(pq)

        if best[c_node][passed] < c_dist: continue

        for n_dist, n_node in graph[c_node]:
            n_passed = passed
            if passed or (c_node, n_node) == (G, H) or (c_node, n_node) == (H, G):
                n_passed = 1

            if best[n_node][n_passed] > n_dist + c_dist:
                best[n_node][n_passed] = n_dist + c_dist
                heapq.heappush(pq, (c_dist + n_dist, n_node, n_passed))

    return best


Test = int(input())

for tc in range(1, Test + 1):
    N, M, T = map(int, input().split())  # n 교차로, m 도로, 목적지 t
    S, G, H = map(int, input().split())  # s 출발지, g -- h

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    destination = []
    for _ in range(T):
        destination.append(int(input()))

    possible_destinations = bfs(S)

    for d in sorted(destination):
        visited = possible_destinations[d][1]
        if visited == min(visited, possible_destinations[d][0]) and visited != float('inf'):
            print(d, end=" ")

    print()
