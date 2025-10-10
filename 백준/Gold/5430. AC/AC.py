"""
백준 - AC
"""
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    p = list(input())
    n = int(input())
    data = input()[1:-1]
    is_reversed = False

    if n == 0:
        q = deque([])
    else:
        q = deque(data.split(','))

    for cmd in p:
        if cmd == 'D':
            if q:
                if is_reversed:
                    q.pop()
                else:
                    q.popleft()
            else:
                print('error')
                break
        else:
            is_reversed = not is_reversed
    else:
        if is_reversed:
            q.reverse()
        answer = ','.join(q)
    
        print(f'[{answer}]')