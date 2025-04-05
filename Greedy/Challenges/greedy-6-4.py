import heapq


def solution(food_times, k):
    answer = 0
    data = []

    for i in range(len(food_times)):
        heapq.heappush(data, (food_times[i], i))
    print(data)
    return answer


print(solution([3, 1, 2], 5))
