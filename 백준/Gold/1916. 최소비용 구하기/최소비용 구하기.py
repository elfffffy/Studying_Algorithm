import heapq

N = int(input())  # 도시의 개수 = 노드의 개수
M = int(input())  # 버스의 개수 = 간선의 개수

# 인접리스트 생성
# alist[출발점] = [(비용1, 도착점1), (비용2, 도착점2)...]
alist = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    alist[start].append((cost, end))

start, end = map(int, input().split())


def bfs(start):
    pq = []
    heapq.heappush(pq, (0, start))
    best = [float('inf')] * (N + 1)

    while pq:
        c_cost, c_start = heapq.heappop(pq)

        if c_start == end:
            return c_cost

        if best[c_start] < c_cost: continue

        for i in range(len(alist[c_start])):
            n_cost, n_start = alist[c_start][i]
            if best[n_start] > n_cost + c_cost:
                heapq.heappush(pq, (n_cost + c_cost, n_start))
                best[n_start] = n_cost + c_cost


print(bfs(start))