import heapq, sys

input = sys.stdin.readline

# 수업의 개수
n = int(input())

# 시간
times = [list(map(int, input().split())) for _ in range(n)]

# 시작 시간을 기준으로 정렬
times.sort()

# 첫 번째로 시작하는 강의 끝나는 시간 넣어주기
# pq => 강의 끝나는 시간이 자동으로 제일 작은 값이 빠져나오게 됨
pq = [times[0][1]]

# 가장 빨리 끝나는 수업 시간이 현재 시작 시간보다 먼저 끝나면 강의실 배정 가능
for i in range(1, n):

    # 끝나는 시간이 다음 시작 시간보다 작거나 같다면 강의실 배정 가능
    # => 원래 있던 끝나는 시간을 빼고 새 끝나는 시간을 추가
    # 끝나는 시간이 다음 시작 시간보다 크다면 강의실 아직 사용중 => 새 강의실 배정
    if pq[0] <= times[i][0]:
        heapq.heappop(pq)
    heapq.heappush(pq, times[i][1])

print(len(pq))