N, X = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = sum(arr[:X])
max_v = sum_v
period = 1

for i in range(N - X):
    flag = False
    sum_v -= arr[i]
    sum_v += arr[i + X]
    if sum_v > max_v:
        max_v = sum_v
        period = 1

    elif sum_v == max_v:
        period += 1

if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(period)