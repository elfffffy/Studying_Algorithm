n, m = map(int, input().split())
j = int(input())
pos = [int(input()) for _ in range(j)]

# 가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.
start = 1
end = m
cnt = 0

for p in pos:
    if start <= p <= end:
        continue
    elif p < start:
        cnt += start - p
        start = p
        end = p + m - 1

    else:
        cnt += p - end
        start = p - m + 1
        end = p

print(cnt)
