"""
백준 - 수학은 비대면강의입니다
"""
a, b, c, d, e, f = map(int, input().split())
x, y = 0, 0

y = (c * d - a * f) // (b * d - a * e)
x = (c * e - b * f) // (a * e - b * d)

print(x, y)