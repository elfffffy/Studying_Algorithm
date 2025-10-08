"""
백준 - 도키도키 간식 드리미
"""
from collections import deque

N = int(input())
q = deque(list(map(int, input().split())))
stack = []
goal = 1
can_get = True

while q:
    student = q[0]
    if q[0] == goal:
        q.popleft()
        goal += 1
    else:
        if stack and stack[-1] == goal:
            stack.pop()
            goal += 1
        else:
            q.popleft()
            stack.append(student)

while stack:
    if stack and stack[-1] == goal:
        stack.pop()
        goal += 1
    else:
        print('Sad')
        can_get = False
        break

if can_get:
    print('Nice')