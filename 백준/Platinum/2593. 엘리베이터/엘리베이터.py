"""
백준 - 엘리베이터
"""
from collections import deque
import math

N, M = map(int, input().split())

elevators = {}  # {엘베번호: (시작층, 간격)}

for i in range(1, M + 1):
    a, b = map(int, input().split())
    elevators[i] = (a, b)

A, B = map(int, input().split())

# A층과 B층에 정차하는 엘리베이터 찾기
start_elevators = []
end_elevators = []

for i in range(1, M + 1):
    a, b = elevators[i]
    if A >= a and (A - a) % b == 0:
        start_elevators.append(i)
    if B >= a and (B - a) % b == 0:
        end_elevators.append(i)


# 두 엘리베이터가 공통 층에서 만나는지 확인
def can_connect(e1, e2):
    a1, b1 = elevators[e1]
    a2, b2 = elevators[e2]

    # 범위 내에서 공통 층이 있는지 확인
    # a1 + k1*b1 == a2 + k2*b2 를 만족하는 k1, k2가 존재하는가?
    # 중국인의 나머지 정리 또는 단순 검색

    max_floor = min(a1 + ((N - a1) // b1) * b1, a2 + ((N - a2) // b2) * b2)

    # 작은 간격의 엘리베이터 기준으로 검색
    if b1 < b2:
        floor = a1
        while floor <= max_floor:
            if floor >= a2 and (floor - a2) % b2 == 0:
                return True
            floor += b1
    else:
        floor = a2
        while floor <= max_floor:
            if floor >= a1 and (floor - a1) % b1 == 0:
                return True
            floor += b2

    return False


# 연결 그래프 구축
connection = [[0] * (M + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    for j in range(i + 1, M + 1):
        if can_connect(i, j):
            connection[i][j] = 1
            connection[j][i] = 1


def can_take():
    if not start_elevators:
        return -1, []

    q = deque()
    parent = {}

    for se_idx in start_elevators:
        q.append((1, se_idx))
        parent[se_idx] = None

    while q:
        cnt, c_idx = q.popleft()

        if c_idx in end_elevators:
            path = []
            elevator = c_idx

            while elevator is not None:
                path.append(elevator)
                elevator = parent[elevator]

            return cnt, path[::-1]

        for n_idx in range(1, M + 1):
            if n_idx in parent:
                continue

            if connection[c_idx][n_idx] == 1:
                q.append((cnt + 1, n_idx))
                parent[n_idx] = c_idx

    return -1, []


min_cnt, route = can_take()

if min_cnt == -1:
    print(-1)
else:
    print(min_cnt)
    for r in route:
        print(r)
