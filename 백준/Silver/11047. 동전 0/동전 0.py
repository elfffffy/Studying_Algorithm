from collections import deque

N, K = map(int, input().split())
values = deque([int(input()) for _ in range(N)])

cnt = 0
while K != 0:
    c_type = values.pop()
    cnt += K // c_type
    K %= c_type

print(cnt)
