n = int(input())
result = 0

three_data = []
t_hour = 0
t_minute = 0
t_second = 0

for i in range(60):
    if '3' in str(i):
        three_data.append(i)

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60) :
            if second in three_data or minute in three_data or hour in three_data :
                result += 1

print(result)
