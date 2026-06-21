def solution(board, skill):
    n, m = len(board), len(board[0])
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for s_type, y1, x1, y2, x2, degree in skill:
        if s_type == 1:
            memo[y1][x1] -= degree
            memo[y1][x2 + 1] += degree
            memo[y2 + 1][x1] += degree
            memo[y2 + 1][x2 + 1] -= degree
        else:
            memo[y1][x1] += degree
            memo[y1][x2 + 1] -= degree
            memo[y2 + 1][x1] -= degree
            memo[y2 + 1][x2 + 1] += degree

    for y in range(n + 1):
        for x in range(m + 1):
            if x == 0: continue
            memo[y][x] += memo[y][x - 1]

    for x in range(m + 1):
        for y in range(n + 1):
            if y == 0: continue
            memo[y][x] += memo[y - 1][x]

    answer = 0
    for by in range(n):
        for bx in range(m):
            final_v = board[by][bx] + memo[by][bx]
            if final_v > 0:
                answer += 1

    return answer