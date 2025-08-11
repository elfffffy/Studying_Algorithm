N = int(input())
info = []

for i in range(N):
    age, name = input().split()
    info.append((int(age), i, name))

info.sort()
for p in info:
    print(p[0], p[2])
