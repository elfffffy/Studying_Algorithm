import sys

sys.setrecursionlimit(10 ** 6)

lst = [int(readline) for readline in sys.stdin]


def func(lst):
    if not lst:
        return

    if len(lst) == 1:
        print(lst[0])
        return

    mid = lst[0]
    left = []
    right = []

    for i in range(1, len(lst)):
        if lst[i] < mid:
            left.append(lst[i])
        else:
            right.append(lst[i])

    func(left)
    func(right)
    print(mid)


func(lst)