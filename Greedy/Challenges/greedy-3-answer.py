data = input()
# 0으로 바꾸는 경우
count0 = 0
# 1로 바꾸는 경우
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
