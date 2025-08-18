# 빠른 입력 사용
import sys

input = sys.stdin.readline

# k 회의실 수
# n 회의 개수
n, k = map(int, input().split())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

time_table = [[] for _ in range(k)]

for start, end in times:
    min_v = 1e9
    min_pos = -1
    for idx, table in enumerate(time_table):
        if not table:
            min_pos = idx

        else:
            if (min_v > start - table[-1][1]) and (table[-1][1] < start):
                min_v = start - table[-1][1]
                min_pos = idx

    if min_pos != -1:
        time_table[min_pos].append((start, end))

cnt = 0
for a in time_table:
    cnt += len(a)

print(cnt)
