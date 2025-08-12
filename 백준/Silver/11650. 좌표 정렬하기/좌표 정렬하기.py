N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

for a in arr:
    print(*a)
