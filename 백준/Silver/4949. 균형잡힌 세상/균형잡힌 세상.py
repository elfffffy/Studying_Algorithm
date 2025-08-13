while True:
    text = input()

    if text == '.':
        break

    stack = []
    ans = 'yes'

    for x in text:
        if x in ['(', '[']:
            stack.append(x)

        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
                break

        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'
                break

    if len(stack) > 0:
        ans = 'no'

    print(ans)
