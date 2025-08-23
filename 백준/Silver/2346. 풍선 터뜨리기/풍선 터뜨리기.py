from collections import deque

N = int(input())

pang = 0
arr = list(map(int, input().split()))

q = deque([(x, i) for i, x in enumerate(arr)])

while q:
    if pang == 0:
        pang_result = q.popleft()
        print(abs(pang_result[1]) + 1, end=" ")
        pang = pang_result[0]
    else:
        if pang < 0:
            for _ in range(abs(pang)):
                q.appendleft(q.pop())
            pang_result = q.popleft()
            print(abs(pang_result[1]) + 1, end=" ")
            pang = pang_result[0]

        else:
            for _ in range(pang - 1):
                q.append(q.popleft())

            pang_result = q.popleft()
            print(abs(pang_result[1]) + 1, end=" ")
            pang = pang_result[0]
