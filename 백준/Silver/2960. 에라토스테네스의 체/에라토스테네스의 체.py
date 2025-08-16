n, k = map(int, input().split())
dat = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if dat[i] == 0:
        for j in range(i, n + 1, i):
            if dat[j] != 1 :
                dat[j] = 1
                cnt += 1

            if cnt == k:
                print(j)
                exit()