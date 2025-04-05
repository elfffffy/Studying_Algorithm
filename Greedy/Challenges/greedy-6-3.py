def solution(food_times, k):
    answer = 0

    while k > 0:
        for i in food_times:
            if i != 0:
                i -= 1
                k -= 1
            answer = i
    return answer

solution([3, 1, 2], 5)

