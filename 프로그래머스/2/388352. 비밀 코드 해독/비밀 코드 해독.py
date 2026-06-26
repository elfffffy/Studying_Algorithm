from itertools import combinations


def solution(n, q, ans):
    nums = [i for i in range(1, n + 1)]
    possible_cases = list(combinations(nums, 5))
    answer = 0

    for case in possible_cases:
        check = 0
        for i in range(len(q)):
            query = q[i]
            q_answer = ans[i]

            cnt = 0
            for x in case:
                for y in query:
                    if x < y: break
                    if x == y:
                        cnt += 1

            if cnt == ans[i]:
                check += 1

        if check == len(q):
            answer += 1

    return answer