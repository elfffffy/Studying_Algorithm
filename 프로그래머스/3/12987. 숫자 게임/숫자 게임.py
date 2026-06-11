def solution(A, B):
    length = len(A)
    A.sort()
    B.sort()
    answer = 0
    b_point = 0

    for i in range(length):
        while b_point < length:
            if A[i] < B[b_point]:
                answer += 1
                b_point += 1
                break
            b_point += 1

    return answer
