"""
소가 길을 건너간 이유 1
"""

N = int(input())
check_list = [[] for _ in range(11)]

for _ in range(N):
    cow, info = map(int, input().split())
    check_list[cow].append(info)

cnt = 0
for c in check_list:
    if c and len(c) >= 2:
        pos = c[0]
        for i in range(1, len(c)):
            if pos != c[i]:
                cnt += 1
            pos = c[i]

print(cnt)