n, m = map(int, input().split())
k = list(map(int, input().split()))
count = 0

for i in range (len(k)) :
    for j in k :
        if k[i] != j :
            count += 1

count = int(count/2)

print(count)