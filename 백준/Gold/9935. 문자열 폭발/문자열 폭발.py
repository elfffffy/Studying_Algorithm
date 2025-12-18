import sys

input = sys.stdin.readline

text = list(input().strip())
target = list(input().strip())

size = len(target)
new_text = []

for char in text:
    new_text.append(char)

    if len(new_text) >= size and new_text[-size:] == target:
        for _ in range(size):
            new_text.pop()


if new_text:
    print(''.join(new_text))
else:
    print('FRULA')