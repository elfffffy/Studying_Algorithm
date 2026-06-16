def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker)

    def find_max(arr):
        dp = [0] * (n - 1)
        dp[0] = arr[0]
        dp[1] = max(dp[0], arr[1])

        for x in range(2, n - 1):
            dp[x] = max(dp[x - 2] + arr[x], dp[x - 1])

        return dp[-1]

    sticker_one = sticker[0: n - 1]
    sticker_two = sticker[1: n]

    sticker_one_sum = find_max(sticker_one)
    sticker_two_sum = find_max(sticker_two)

    answer = max(sticker_one_sum, sticker_two_sum)
    return answer