N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
answer = []

for person in arr:
    cnt = 1
    for c_person in arr:
        if person == c_person:
            continue
        else:
            if person[0] < c_person[0] and person[1] < c_person[1]:
                cnt += 1

    answer.append(cnt)

print(*answer)
