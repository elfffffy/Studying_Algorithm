"""🗝️해설 참조
완전 탐색을 이용해서 열쇠를 이동하거나 회전시켜 자물쇠를 끼워보는 작업을 시도하기
자물쇠가 3 * 3 크기일 때, 크기가 3배인 새로운 리스트로 만들어서 중앙 부분으로 옮긴다.
이후 열쇠 배열을 왼쪽에서 시작해서 한 칸씩 이동하는 방식으로 확인한다.
"""

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90deg(a) :
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
            return True

def solution(key, lock) :
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range (n) :
        for j in range(m) :
            new_lock[i+n][j+n] = lock[i][j]
            
    #4가지 방향에 대해서 확인하기
    for rotation in range (4) :
        key = rotate_a_matrix_by_90deg(key) #열쇠 회전
        # new_lock에서 x는 행, y는 열
        for x in range (n*2) :
            for y in range(m*2) :
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]
                
                # 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True :
                    return True

                # 자물쇠에 열쇠 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] -= key[i][j]
    return False


x = [[0,0,0], [1,0,0], [0,1,1]]
y = [[1,1,1], [1,1,0], [1,0,1]]
a = solution(x, y)

print(a)