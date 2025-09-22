"""
백준 - 가장 가까운 공통 조상
"""
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(son):
    global ancestor

    ancestor.append(son)

    for i in range(len(arr[son])):
        dfs(arr[son][i])

    return


def dfs2(son):
    global find_ancestor

    if son in ancestor:
        print(son)
        find_ancestor = True
        return

    for i in range(len(arr[son])):
        dfs2(arr[son][i])
        if find_ancestor:
            return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        arr[b].append(a)

    tar1, tar2 = map(int, input().split())

    ancestor = []
    dfs(tar1)

    find_ancestor = False
    dfs2(tar2)
