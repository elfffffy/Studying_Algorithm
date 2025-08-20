from collections import deque

N = int(input())
arr = [x for x in range(1, N + 1)]
dq = deque(arr)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])