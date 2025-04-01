def solution(food_times, k):
    answer = 0
    


    while k > 0:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                k -= 1
                food_times[i] -= 1
            answer = i
    if answer == len(food_times) - 1:
        answer = 1

    return answer


solution([3, 1, 2], 5)
