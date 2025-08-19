N, L = map(int, input().split())
height = list(map(int, input().split()))
height.sort()
total = L

for i in height:
    if total >= i:
        total += 1
    else:
        break

print(total)