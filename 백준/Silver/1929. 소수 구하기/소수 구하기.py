m, n = map(int, input().split())
dat = [0] * (n + 1)
dat[0] = dat[1] = 1

for i in range(2, n + 1):
    if dat[i] == 0:
        for j in range(i * 2, n + 1, i):
            if dat[j] != 1:
                dat[j] = 1

for i in range(m, n + 1):
    if dat[i] == 0:
        print(i)