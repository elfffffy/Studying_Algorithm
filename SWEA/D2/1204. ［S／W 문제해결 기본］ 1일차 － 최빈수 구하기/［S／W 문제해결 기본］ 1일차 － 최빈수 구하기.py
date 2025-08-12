T = int(input())
for tc in range(1, T + 1):
    TN = int(input())
    scores = list(map(int, input().split()))

    dat = [0] * 101

    for score in scores:
        dat[score] += 1

    dat.reverse()
    print(f'#{TN} {100 - dat.index(max(dat))}')