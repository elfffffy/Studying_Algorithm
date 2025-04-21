def solution(s):
    # answer에 최대 문자열의 길이가 들어간다.
    answer = len(s)
    
    # step = 묶음 단위
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        # 기준이 되는 step 길이의 문자열 추출한다.
        prev = s[0:step]
        count = 1

        # step 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 문자열과 같다면 count 값만 변경한다.
            if prev == s[j:j + step]:
                count += 1
            # 이전 문자열과 다르다면, compressed 변수에 압축한 결과를 넣어준다.
            else:
                # 삼항연산자를 사용해서, count가 1이면 prev 값만 나올 수 있도록 한다.
                compressed += str(count) + prev if count >= 2 else prev
                # prev 값을 새로운 값으로 갱신한다.
                prev = s[j:j + step]
                count = 1
        # step만큼 묶고 남은 문자열에 대해서 따로 더해준다.
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer