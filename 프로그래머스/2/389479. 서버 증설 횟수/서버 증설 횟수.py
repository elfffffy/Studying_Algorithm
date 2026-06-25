from collections import defaultdict


def solution(players, m, k):
    answer = 0
    server_cnt = 0
    server_time_limit = defaultdict()

    for t in range(24):
        if t in server_time_limit.keys():
            server_cnt -= server_time_limit[t]
        if players[t] < m or players[t] < m * server_cnt + 1:
            continue

        new_server_cnt = players[t] // m - server_cnt
        if new_server_cnt:
            server_cnt += new_server_cnt
            answer += new_server_cnt
            server_time_limit[t + k] = new_server_cnt

    return answer