n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)

result = 0
except_first = 0

if 1 in data :
    for i in range(1, len(data)) :
        except_first += data[i]
    if except_first <= data[0]:
        result = except_first
    else:
        result = except_first + data[0]
else :
    result = 0

print(result + 1)