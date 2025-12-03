"""
백준 - 2048
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]


#  상 하 좌 우 = 0 1 2 3
def push(direction, board):
    working_board = [row[:] for row in board]
    if direction == 0:
        for x in range(N):
            except_zero = []
            for y in range(N):
                if working_board[y][x] == 0: continue
                except_zero.append(working_board[y][x])

            sum_result_list = []

            if len(except_zero) == 1:
                sum_result_list.append(except_zero[0])

            else:
                i = 0
                while i < len(except_zero):
                    if (i + 1 < len(except_zero)) and except_zero[i] == except_zero[i + 1]:
                        sum_result_list.append(except_zero[i] * 2)
                        i += 2
                    else:
                        sum_result_list.append(except_zero[i])
                        i += 1

            for y in range(N):
                if y <= len(sum_result_list) - 1:
                    working_board[y][x] = sum_result_list[y]
                else:
                    working_board[y][x] = 0

    elif direction == 1:
        for x in range(N):
            except_zero = []
            for y in range(N - 1, -1, -1):
                if working_board[y][x] == 0: continue
                except_zero.append(working_board[y][x])

            sum_result_list = []

            if len(except_zero) == 1:
                sum_result_list.append(except_zero[0])

            else:
                i = 0
                while i < len(except_zero):
                    if (i + 1 < len(except_zero)) and except_zero[i] == except_zero[i + 1]:
                        sum_result_list.append(except_zero[i] * 2)
                        i += 2
                    else:
                        sum_result_list.append(except_zero[i])
                        i += 1

            j = 0
            for y in range(N - 1, -1, -1):
                if y < N - len(sum_result_list):
                    working_board[y][x] = 0
                else:
                    working_board[y][x] = sum_result_list[j]
                    j += 1

    elif direction == 2:
        for y in range(N):
            except_zero = []
            for x in range(N):
                if working_board[y][x] == 0: continue
                except_zero.append(working_board[y][x])

            sum_result_list = []

            if len(except_zero) == 1:
                sum_result_list.append(except_zero[0])

            else:
                i = 0
                while i < len(except_zero):
                    if (i + 1 < len(except_zero)) and except_zero[i] == except_zero[i + 1]:
                        sum_result_list.append(except_zero[i] * 2)
                        i += 2
                    else:
                        sum_result_list.append(except_zero[i])
                        i += 1

            for x in range(N):
                if x <= len(sum_result_list) - 1:
                    working_board[y][x] = sum_result_list[x]
                else:
                    working_board[y][x] = 0

    else:
        for y in range(N):
            except_zero = []
            for x in range(N - 1, -1, -1):
                if working_board[y][x] == 0: continue
                except_zero.append(working_board[y][x])

            sum_result_list = []

            if len(except_zero) == 1:
                sum_result_list.append(except_zero[0])

            else:
                i = 0
                while i < len(except_zero):
                    if (i + 1 < len(except_zero)) and except_zero[i] == except_zero[i + 1]:
                        sum_result_list.append(except_zero[i] * 2)
                        i += 2
                    else:
                        sum_result_list.append(except_zero[i])
                        i += 1

            j = 0
            for x in range(N - 1, -1, -1):
                if x < N - len(sum_result_list):
                    working_board[y][x] = 0
                else:
                    working_board[y][x] = sum_result_list[j]
                    j += 1

    return working_board


def play(cnt, board):
    global max_v
    before_board = [row[:] for row in board]

    if cnt == 5:
        value = float('-inf')
        for b in board:
            value = max(value, max(b))
        max_v = max(value, max_v)
        return

    for i in range(4):
        after_board = push(i, before_board)
        play(cnt + 1, after_board)


max_v = float('-inf')
play(0, MAP)
print(max_v)
