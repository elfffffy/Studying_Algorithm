n, k = map(int, input().split())
dat = [[0] * 2 for _ in range(7)]

for _ in range(n):
    gender, grade = map(int, input().split())
    dat[grade][gender] += 1

cnt = 0
for i in range(1, 7):
    for g in range(2):
        cnt += (dat[i][g] // k) + (dat[i][g] % k)

print(cnt)