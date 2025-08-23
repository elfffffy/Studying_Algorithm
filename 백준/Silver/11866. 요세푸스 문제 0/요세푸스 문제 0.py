from collections import deque

N, K = map(int, input().split())

now = K
q = deque([x for x in range(1, N + 1)])

answer = []
while q:
    for _ in range(K - 1):
        q.append(q.popleft())

    answer.append(str(q.popleft()))

print(f'<{', '.join(answer)}>')
