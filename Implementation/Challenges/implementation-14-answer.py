from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배 늘려서 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    # answer(투입 되는 친구의 수)의 최댓값은 len(dist)이기 때문에 최솟값을 구하기 위해 1을 더해준다.
    answer = len(dist) + 1
    # 0부터 length = 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):  # length만큼 묶이면 무조건 한 묶음의 weak가 된다.
                if position < weak[index]:
                    count += 1  # 새로운 친구 추가
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer