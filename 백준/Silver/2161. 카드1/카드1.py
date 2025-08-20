from collections import deque

N = int(input())
arr = [x for x in range(1, N + 1)]
dq = deque(arr)
floor = []

while len(dq) > 1:
    floor.append(dq.popleft())
    dq.append(dq.popleft())

print(*floor, dq[0])