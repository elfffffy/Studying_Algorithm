import sys, heapq

input = sys.stdin.readline

# 연산의 개수
N = int(input())

# 배열 생성
pq = []

for _ in range(N):
    num = int(input())

    # num이 0이 아니라면 추가하기
    if num != 0:
        heapq.heappush(pq, (abs(num), num))

    # num이 0이라면, 절댓값이 가장 작은 값 출력 및 제거
    else:

        # pq에 요소가 있는 경우
        if pq:
            min_v = heapq.heappop(pq)
            print(min_v[1])

        # pq에 요소가 없는 경우
        else:
            print(0)
