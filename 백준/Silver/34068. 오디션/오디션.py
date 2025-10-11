import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dat = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    dat[a] += 1

sorted_dat = sorted(dat[1:])
cnt = 0
for i in range(N - 1):
    if sorted_dat[i] < sorted_dat[i + 1]: continue
    cnt += (sorted_dat[i] + 1 - sorted_dat[i + 1])
    sorted_dat[i + 1] = sorted_dat[i] + 1
print(cnt)