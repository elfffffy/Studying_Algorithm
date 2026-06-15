def solution(n, stations, w):
    answer = 0
    max_range = 2 * w + 1
    start = 1

    for i in stations:
        range_start = i - w
        range_end = i + w

        need = range_start - start

        if need > 0:
            answer += (need + max_range - 1) // max_range

        start = range_end + 1

    if start <= n:
        need = n - start + 1
        answer += (need + max_range - 1) // max_range

    return answer