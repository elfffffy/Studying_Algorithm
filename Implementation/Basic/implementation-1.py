n = int(input())
data = list(input().split())

x = 1
y = 1

for i in data :
    if i == 'R' :
        if y != n :
            y += 1
    elif i == 'L' :
        if y != 1:
            y -= 1
    elif i == 'U' :
        if x != 1:
            x -= 1
    else :
        if x != n:
            x += 1

print(x, y)