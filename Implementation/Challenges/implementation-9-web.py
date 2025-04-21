def solution(s):
    data = s
    cutting = len(data) // 2
    store = [[] for _ in range(cutting)]
    while cutting > 0:
        a = len(data) // cutting
        b = len(data) % cutting

        for i in range(a):
            if i == 0:
                store[cutting - 1].append(data[0:cutting])
            else:
                store[cutting - 1].append(data[i * cutting:i * cutting + cutting])
        if b != 0:
            store[cutting - 1].append(data[a * cutting:])

        cutting -= 1

    answer = 0
    for i in store:
        value = ""
        result_list = []
        result = 1
        for j in i:
            if j == value:
                result += 1
                continue
            else:
                if value != "":
                    if result == 1:
                        result_list.append(value)
                    else:
                        result_list.append(str(result) + value)
                value = j
                result = 1
        if result == 1:
            result_list.append(value)
        else:
            result_list.append(str(result) + value)

        if answer == 0:
            answer = len(''.join(result_list))
        else:
            answer = min(answer, len(''.join(result_list)))
    return answer