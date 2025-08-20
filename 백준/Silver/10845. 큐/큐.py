from collections import deque


def push(x):
    arr.append(x)


def pop():
    if arr:
        return arr.popleft()
    else:
        return -1


def size():
    return len(arr)


def empty():
    if arr:
        return 0
    else:
        return 1


def front():
    if arr:
        return arr[0]
    else:
        return -1


def back():
    if arr:
        return arr[-1]
    else:
        return -1


N = int(input())
arr = deque()
answer = []

for _ in range(N):
    text = input()
    if " " in text:
        cmd, num = text.split()
    else:
        cmd = text



    if cmd == 'push':
        push(int(num))

    elif cmd == 'front':
        answer.append(front())

    elif cmd == 'back':
        answer.append(back())

    elif cmd == 'size':
        answer.append(size())

    elif cmd == 'empty':
        answer.append(empty())

    elif cmd == 'pop':
        answer.append(pop())

print(*answer, sep="\n")