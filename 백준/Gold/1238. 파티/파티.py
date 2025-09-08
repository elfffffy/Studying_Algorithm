import heapq


def bfs(x, arr):
    dist = [float('inf')] * (n + 1)
    # 처음 위치
    dist[x] = 0
    pq = [(0, x)]

    while pq:
        c_distance, c_node = heapq.heappop(pq)

        if c_distance > dist[c_node]: continue

        for node, value in arr[c_node]:
            distance = value + c_distance

            if distance < dist[node]:
                dist[node] = distance
                heapq.heappush(pq, (distance, node))
    return dist


# n: 마을 및 학생 수
# m: 간선의 수 (단방향)
# x: 파티가 열리는 마을
n, m, x = map(int, input().split())

# 인접리스트 생성
# alist[시작점] = (끝 점, 소요 시간)
alist = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    alist[start].append((end, time))

total_time = [[]]
for i in range(1, n + 1):
    total_time.append(bfs(i, alist))

students = [0] * (n + 1)
for i in range(1, n + 1):
    students[i] = total_time[i][x] + total_time[x][i]

print(max(students))
