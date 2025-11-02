"""
백준 - 베스트셀러
"""
from collections import defaultdict

N = int(input())

my_dict = defaultdict(int)
for _ in range(N):
    text = input()
    my_dict[text] += 1

max_value = float('-inf')
max_key = ""
for key, value in my_dict.items():
    if max_value < value:
        max_value = value
        max_key = key

    elif (max_value == value) and (max_key > key):
        max_key = key

print(max_key)