N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

dat = [0] * 20000001

for i in N_arr:
    dat[i] += 1

for j in M_arr:
    print(dat[j], end=" ")
