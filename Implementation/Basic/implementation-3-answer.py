input_data = input()

# row = 열 = 숫자
row = int(input_data[1])
# column = 행 = 알파벳
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 이동할 수 있는 방향 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동가능 여부 확인
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
