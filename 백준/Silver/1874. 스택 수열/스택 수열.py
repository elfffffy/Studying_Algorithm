n = int(input())

target_list = [int(input()) for _ in range(n)]
stack = []
answer = []
num = 1

for target in target_list:
    while num <= target:
        stack.append(num)
        answer.append('+')
        num += 1

    if stack[-1] == target:
        stack.pop()
        answer.append('-')

    else:
        print('NO')
        answer.clear()
        break

if answer:
    for op in answer:
        print(op)