N = int(input()) # 6
stairs = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)

if N == 1:
    print(stairs[1])

elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])
    
    print(dp[-1])