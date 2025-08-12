import sys
input = sys.stdin.readline

class Stack:
    def __init__(self, s_stack):
        self.s_stack = s_stack

    def push(self, s_num):
        self.s_stack.append(s_num)

    def pop(self):
        if self.s_stack:
            print(self.s_stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.s_stack))

    def empty(self):
        if self.s_stack:
            print(0)
        else:
            print(1)

    def top(self):
        if self.s_stack:
            print(self.s_stack[-1])
        else:
            print(-1)


N = int(input())
stack = []
my_stack = Stack(stack)

for _ in range(N):
    cmd_num = input().strip()
    if " " in cmd_num:
        cmd, num = cmd_num.split()
    else:
        cmd = cmd_num

    if cmd == 'push':
        my_stack.push(int(num))

    elif cmd == 'top':
        my_stack.top()

    elif cmd == 'size':
        my_stack.size()

    elif cmd == 'empty':
        my_stack.empty()

    elif cmd == 'pop':
        my_stack.pop()
