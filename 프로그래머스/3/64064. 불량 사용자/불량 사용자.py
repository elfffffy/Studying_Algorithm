def solution(user_id, banned_id):
    cases = [[] for _ in range(len(banned_id))]

    start = 0

    for ban in banned_id:
        for user in user_id:
            if len(ban) != len(user): continue
            check = True
            for i in range(len(user)):
                if ban[i] == '*': continue
                if user[i] != ban[i]:
                    check = False
                    break
            if check:
                cases[start].append(user)

        start += 1

    def dfs(x):
        if x == len(cases):
            all_combinations.add(frozenset(temp_group))
            return

        for i in range(len(cases[x])):
            name = cases[x][i]
            if name in temp_group: continue
            temp_group.append(name)
            dfs(x + 1)
            temp_group.pop()

    temp_group = []
    all_combinations = set()
    dfs(0)
    answer = len(all_combinations)
    return answer