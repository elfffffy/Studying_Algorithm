"""
백준 - 구슬 찾기
플로이드워셔을 써서 각 노드간 무게 비교할 때, 가운데 들어갈 수 있는지 없는지 판별
한 가지 경우라도 있다면 답 카운트 x
"""
from collections import deque

N, M = map(int, input().split())
small = [[] for _ in range(N + 1)]
big = [[] for _ in range(N + 1)]

for _ in range(M):
    heavy, light = map(int, input().split())
    small[heavy].append(light)
    big[light].append(heavy)


def bfs(i, arr):
    q = deque()
    q.append(i)
    visited = [0] * (N + 1)
    visited[i] = 1
    cnt = 0

    while q:
        node = q.popleft()
        for n_node in arr[node]:
            if visited[n_node] == 1: continue
            q.append(n_node)
            visited[n_node] = 1
            cnt += 1
    return cnt


result = 0
for i in range(1, N + 1):
    small_cnt = bfs(i, small)
    big_cnt = bfs(i, big)
    if small_cnt > (N - 1) // 2 or big_cnt > (N - 1) // 2:
        result += 1

print(result)