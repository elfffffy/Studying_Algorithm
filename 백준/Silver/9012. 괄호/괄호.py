T = int(input())

for tc in range(1, T + 1):
    text = input()

    if text == '.':
        break

    stack = []
    ans = 'YES'

    for x in text:
        if x == '(':
            stack.append(x)

        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'NO'
                break

    if len(stack) > 0:
        ans = 'NO'

    print(ans)

