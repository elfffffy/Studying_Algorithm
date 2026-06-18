from collections import defaultdict


def solution(gems):
    gems_type = set(gems)
    total_gems = len(gems_type)

    d = defaultdict(int)
    types = 0
    left = 0

    answer = [1, len(gems)]
    min_length = len(gems)

    for right in range(len(gems)):
        if d[gems[right]] == 0:
            types += 1
        d[gems[right]] += 1

        while types == total_gems:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                answer = [left + 1, right + 1]

            d[gems[left]] -= 1
            if d[gems[left]] == 0:
                types -= 1
            left += 1

    return answer
