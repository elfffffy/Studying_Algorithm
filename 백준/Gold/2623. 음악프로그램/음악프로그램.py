"""
백준 - 음악 프로그램
"""
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(1, data[0]):
        graph[data[i]].append(data[i + 1])
        indegree[data[i + 1]] += 1

zeros = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        zeros.append(i)

start = zeros[0]
if len(zeros) > 1:
    for i in range(1, len(zeros)):
        graph[start].append(zeros[i])
        indegree[zeros[i]] += 1

q = deque()
q.append(start)
answer = []
while q:
    c_node = q.popleft()
    answer.append(c_node)
    for n_node in graph[c_node]:
        indegree[n_node] -= 1
        if indegree[n_node] == 0:
            q.append(n_node)

if len(answer) == N:
    print(*answer, sep='\n')
else:
    print(0)