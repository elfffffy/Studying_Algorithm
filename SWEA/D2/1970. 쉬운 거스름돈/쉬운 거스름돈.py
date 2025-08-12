money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')

    N = int(input())

    for m in money:
        print(N // m, end=" ")
        N %= m
    print()