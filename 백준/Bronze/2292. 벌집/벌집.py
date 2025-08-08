num = int(input())

t = 7
cnt = 1
p = 2
if num == 1:
    print(1)
elif 1 < num <= t:
    print(2)
else:
    while t < num:
        cnt += 1
        t += 6 * p
        p += 1

    print(cnt + 1)
