def rotate_a_matrix_by_90deg(a) :
    n = len(a) #행 길이 계산
    m = len(a[0]) #열 길이 계산
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m) :
            # 열이 0이었던 요소들은 행이 1인 자리로 간다.
            # 열이 1인 요소들은 행이 0인 자리로 간다.
            result[j][n-i-1] = a[i][j] #시작은 0이기 때문에 -1을 더 계산 해준다.

    return result