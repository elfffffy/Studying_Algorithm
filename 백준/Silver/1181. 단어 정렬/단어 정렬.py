N = int(input())
text_list = set()

for i in range(N):
    text = input()
    text_list.add((len(text), text))

text_list = list(text_list)
text_list.sort()

for text in text_list:
    print(text[1])
