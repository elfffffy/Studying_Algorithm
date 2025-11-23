"""
달빛 여우

1 --> 4
여우 : 7/2 = 3.5
늑대 : (2/4) + (2/1) + (4/4) = 3.5
=> 최소 거리가 최소 시간을 보장하지 않는다.

그렇다면..!
여우는 다익스트라 쓰고, 늑대는 dfs......?

시간초과...

그렇다면..!
늑대는 짝수일 때 홀수 일 때 나누면 되지 않을까...?

시간 초과 * 8
왜?????????
GPT가 float 계산 때문이라네요,,,
여우는 dist / 2 → 4배 -> dist * 2
늑대는
0(빠름) : dist / 4 -> 4배 -> dist
1(느림) : dist / 1 -> 4배 -> dist * 4
"""
import heapq, sys

input = sys.stdin.readline


def fox_route():
    pq = [(0, 1)]
    fox_best = [float('inf') for _ in range(N + 1)]
    fox_best[1] = 0

    while pq:
        c_time, c_pos = heapq.heappop(pq)

        if c_time > fox_best[c_pos]: continue

        for n_pos, dist in graph[c_pos]:
            n_time = c_time + (dist * 2)

            if n_time < fox_best[n_pos]:
                heapq.heappush(pq, (n_time, n_pos))
                fox_best[n_pos] = n_time

    return fox_best


def wolf_route():
    pq = [(0, 0, 1)]  # 0 빠름 / 1 느림
    wolf_best = [[float('inf'), float('inf')] for _ in range(N + 1)]
    wolf_best[1][0] = 0

    while pq:
        c_time, c_move, c_pos = heapq.heappop(pq)

        if c_time > wolf_best[c_pos][c_move]: continue

        for n_pos, dist in graph[c_pos]:
            if c_move == 0:
                n_time = c_time + dist * 1
                if n_time < wolf_best[n_pos][1]:
                    wolf_best[n_pos][1] = n_time
                    heapq.heappush(pq, (n_time, 1, n_pos))
            else:
                n_time = c_time + dist * 4
                if n_time < wolf_best[n_pos][0]:
                    wolf_best[n_pos][0] = n_time
                    heapq.heappush(pq, (n_time, 0, n_pos))

    return wolf_best


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

fox = fox_route()
wolf = wolf_route()

result = 0
for i in range(1, N + 1):

    if min(wolf[i][0], wolf[i][1]) > fox[i]:
        result += 1

print(result)