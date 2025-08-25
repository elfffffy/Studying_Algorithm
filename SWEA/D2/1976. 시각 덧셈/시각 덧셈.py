T = int(input())

for tc in range(1, T + 1):
    h1, min1, h2, min2 = map(int, input().split())

    hours = h1 + h2
    minutes = min1 + min2

    while minutes >= 60:
        hours += minutes // 60
        minutes -= 60

    if hours >= 13:
        hours -= 12
    print(f'#{tc} {hours} {minutes}')
