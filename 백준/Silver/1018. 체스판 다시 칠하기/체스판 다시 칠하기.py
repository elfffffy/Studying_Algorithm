N, M = map(int, input().split())
boards = [list(input()) for _ in range(N)]
colors = [['W', "B"], ["B", "W"]]

result = float('inf')
for c in range(2):

    for y in range(N - 8 + 1):
        for x in range(M - 8 + 1):
            cnt = [0, 0]
            # (0,0), (0,2), ... (1,1) (1,3)
            for i in range(y, y + 8):
                if i % 2 == 0:
                    for j in range(x, x + 8, 2):
                        if boards[i][j] != colors[c][0]:
                            cnt[c] += 1
                else:
                    for j in range(x + 1, x + 8, 2):
                        if boards[i][j] != colors[c][0]:
                            cnt[c] += 1

            # (0,1), (0,3), ... (1,0) (1,2)
            for i in range(y, y + 8):
                if i % 2 == 0:
                    for j in range(x + 1, x + 8, 2):
                        if boards[i][j] != colors[c][1]:
                            cnt[c] += 1
                else:
                    for j in range(x, x + 8, 2):
                        if boards[i][j] != colors[c][1]:
                            cnt[c] += 1

            result = min(result, cnt[c])

print(result)
