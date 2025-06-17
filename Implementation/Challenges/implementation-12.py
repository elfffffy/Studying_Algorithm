# data = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#         [3, 2, 1, 1]]

data = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
        [1, 1, 1, 0], [2, 2, 0, 1]]

answer = []
column_list = []
row_list = []


def check_column(x, y, types, put_out):
    if put_out == 1:
        if y == 0 or [x - 1, y] in row_list or [x + 1, y] in row_list or [x, y - 1] in column_list:
            answer.append([x, y, types])
            column_list.append([x, y])
            column_list.append([x, y + 1])
    if put_out == 0:

        if [x - 1, y + 1] in row_list and [x + 1, y + 1] in row_list:
            answer.remove([x, y, types])
            column_list.remove([x, y])
            column_list.remove([x, y + 1])


def check_row(x, y, types, put_out):
    if put_out == 1:
        if [x, y - 1] in column_list or [x + 1, y - 1] in column_list or (
                [x - 1, y] in row_list and [x + 1, y] in row_list) :
            answer.append([x, y, types])
            row_list.append([x, y])
            row_list.append([x + 1, y])
    if put_out == 0:
        if [x - 1, y] in column_list and [x + 1, y] in column_list:
            answer.remove([x, y, types])
            row_list.remove([x, y])
            row_list.remove([x + 1, y])


def solution(n, build_frame):
    for i in range(len(data)):
        x = data[i][0]
        y = data[i][1]
        types = data[i][2]
        put_out = data[i][3]

        if types == 0:
            check_column(x, y, types, put_out)
        else:
            check_row(x, y, types, put_out)

    answer.sort()

    return answer


print(solution(5, data))
