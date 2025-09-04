import heapq, sys

input = sys.stdin.readline


def bfs(now):
    best[now] = 0
    pq = [(0, now)]

    while pq:
        c_value, c_node = heapq.heappop(pq)

        if best[c_node] < c_value: continue

        for n_value, n_node in alist[c_node]:
            sum_v = c_value + n_value

            if sum_v < best[n_node]:
                best[n_node] = sum_v
                heapq.heappush(pq, (sum_v, n_node))


v, e = map(int, input().split())
k = int(input())
alist = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    alist[a].append((c, b))

best = [float('inf') for _ in range(v + 1)]
bfs(k)

for i in range(1, v + 1):
    if best[i] == float('inf'):
        print('INF')
    else:
        print(best[i])
