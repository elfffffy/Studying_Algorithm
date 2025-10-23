"""
swea - 벌꿀채취
"""
import itertools

T = int(input())


def calc(lst):
    result = 0
    for i in lst:
        result += i ** 2
    return result


def pick_calc(lst):
    picks = []
    max_v = 0

    for i in range(1, M):
        picks.extend(list(itertools.combinations(lst, i)))

    for pick in picks:
        if sum(pick) <= C:
            sum_v = 0
            for i in pick:
                sum_v += i ** 2
            max_v = max(max_v, sum_v)
    return max_v


for tc in range(1, T + 1):
    # N : 벌통의 크기
    # M : 선택할 수 있는 벌통의 개수
    # C : 꿀을 채취할 수 있는 최대 양
    N, M, C = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for y in range(N):
        for x in range(N - M + 1):
            for y2 in range(y + 1, N):
                for x2 in range(N - M + 1):
                    sum_v = 0
                    a = honeycomb[y][x:x + M]
                    b = honeycomb[y2][x2:x2 + M]

                    if sum(a) <= C:
                        sum_v += calc(a)
                    else:
                        sum_v += pick_calc(a)

                    if sum(b) <= C:
                        sum_v += calc(b)

                    else:
                        sum_v += pick_calc(b)

                    max_v = max(max_v, sum_v)

    for y in range(N):
        for x in range(N - M + 1):
            for x2 in range(x + M, N - M + 1):
                a = honeycomb[y][x:x + M]
                b = honeycomb[y][x2:x2 + M]

                sum_v = 0
                if sum(a) <= C:
                    sum_v += calc(a)
                else:
                    sum_v += pick_calc(a)

                if sum(b) <= C:
                    sum_v += calc(b)

                else:
                    sum_v += pick_calc(b)

                max_v = max(max_v, sum_v)

    print(f'#{tc} {max_v}')