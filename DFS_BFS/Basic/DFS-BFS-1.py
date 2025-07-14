from collections import deque

def check_zero(x, y):
    global graph
    global n
    global m
    answer = []
    if (0 <= x + 1 <= n - 1) and graph[x + 1][y] == 0:
        answer.append((x + 1, y))
    if (0 <= x - 1 <= n - 1) and graph[x - 1][y] == 0:
        answer.append((x - 1, y))
    if (0 <= y + 1 <= m - 1) and graph[x][y + 1] == 0:
        answer.append((x, y + 1))
    if (0 <= y - 1 <= m - 1) and graph[x][y - 1] == 0:
        answer.append((x, y - 1))
    return answer

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n) :
    data = input()
    for j in data :
        graph[i].append(int(j))

zeroList = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeroList.append((i, j))

visited = [[False] * m for _ in range(n)]
finalAnswer = []

while zeroList:
    iceCream = set()
    start = zeroList[0]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        v = queue.popleft()
        vx = v[0]
        vy = v[1]
        if graph[vx][vy] == 0:
            iceCream.add((vx, vy))
            zeroList.remove((vx, vy))
            result = check_zero(vx, vy)
            for i in result:
                if i not in iceCream:
                    queue.append(i)
                    iceCream.add(i)
                    visited[i[0]][i[1]] = True
    finalAnswer.append(iceCream)

print(len(finalAnswer))
