"""
백준 - 트리
"""


def dfs(start):
    global cnt
    visited[start] = 1

    sons = []
    for i in range(N):
        if tree[i] == start and i != erase:
            sons.append(i)

    if not sons:
        cnt += 1
        return

    for son in sons:
        if visited[son]: continue
        dfs(son)


# 노드의 개수
N = int(input())

# 각 노드의 부모
# 없으면 -1
tree = list(map(int, input().split()))

# 지울 노드의 번호
erase = int(input())

cnt = 0
start = 0

for idx, v in enumerate(tree):
    if v == -1:
        start = idx
        break

visited = [0] * N

if start == erase:
    print(0)
else:
    dfs(start)
    print(cnt)
