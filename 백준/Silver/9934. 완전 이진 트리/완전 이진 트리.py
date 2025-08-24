K = int(input())
arr = list(map(int, input().split()))

# 층별 출력값 받을 리스트 생성
answer = [[] for _ in range(K)]


def dfs(arr, lev):

    # 루트 노드 인덱스
    mid = len(arr) // 2
    answer[lev].append(arr[mid])

    if len(arr) == 1:
        return

    dfs(arr[:mid], lev + 1)
    dfs(arr[mid + 1:], lev + 1)

dfs(arr, 0)

for a in answer:
    print(*a)
