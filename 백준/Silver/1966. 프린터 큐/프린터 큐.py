from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    q = deque()
    for idx, num in enumerate(num_list):
        q.append((num, idx))

    cnt = 0

    while q:
        max_v = max(q)[0]

        now = q[0]
        if now[0] < max_v:
            q.append(q.popleft())
        else:
            q.popleft()
            cnt += 1
            if M == now[1]:
                break

    print(cnt)
