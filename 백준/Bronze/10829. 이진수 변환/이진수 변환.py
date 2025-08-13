N = int(input())

stack = []

while True :
    if N == 0:
        break
    stack.append(N % 2)
    N //= 2

while stack :
    print(stack.pop(), end="")