import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야함 => 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    '''
    힙을 사용할 때는 print(q) 보다 heappop()을 이용하는 것이 좋다!
    힙은 내부적으로 이진 트리 구조를 유지하며 데이터를 저장해서 리스트에 삽입된 순서에 따라 이상하게 보일 수 있다.
    
    while q:
        print(heapq.heappop(q))
    '''
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    length = len(food_times)  # 남은 음식의 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K비교
    while sum_value + ((q[0][0] - previous) * length) <= k: # q[0][0] → 항상 힙에서 가장 작은 원소의 첫 번째 값! 하나씩 꺼내는 형식!
        now = heapq.heappop(q)[0]  # heapq.heappop(q) : 제일 작은 원소 + [0] : 첫번째 원소
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    answer = sorted(q, key=lambda x: x[1])  # 음식 번호 기준으로 정렬

    return answer[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))
