def solution(food_times, k):
    answer = 0
    while k > 0:
        for i in range(len(food_times)):
            k -= 1
            if food_times[i] != 0:
                food_times[i] -= 1
                if i == len(food_times) -1 :
                    answer = 1
                else :
                    answer = i + 1
    return answer


print(solution([3, 1, 2], 5))
