# 빠른 입력 사용
import sys
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()
print(*numbers, sep="\n")