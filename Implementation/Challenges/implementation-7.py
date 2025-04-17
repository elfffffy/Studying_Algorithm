n = int(input())
data = []
front = 0
back = 0

for i in str(n) :
    data.append(int(i))

mid = (len(data)) // 2

for value in data[:mid] :
    front += value

for value in data[mid:] :
    back += value

if front == back :
    print('LUCKY')
else :
    print('READY')