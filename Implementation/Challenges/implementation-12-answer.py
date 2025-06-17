# 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 기둥
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame

        # 삭제
        if operate == 0:
            answer.remove([x, y, stuff])  # 일단 삭제
            if not possible(answer):  # 가능한 구조물인지 확인
                answer.append([x, y, stuff])  # 가능하지 않다면, 원상 복구

        # 설치
        if operate == 1:
            answer.append([x, y, stuff]) # 일단 설치
            if not possible(answer) :
                answer.remove([x, y, stuff])

    return sorted(answer)
