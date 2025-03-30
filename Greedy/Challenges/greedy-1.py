people = int(input())
scaryList = list(map(int, input().split()))

scaryList.sort(reverse=True)
result = 0
starting_point = 0

while True :
    if starting_point >= len(scaryList):
        break

    elif scaryList[starting_point] == 1 :
        result += people
        break
    else :
        first = scaryList[starting_point]
        result += 1
        people = people - first
        starting_point += first

print(result)
