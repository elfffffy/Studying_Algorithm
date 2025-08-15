def solution(data, ext, val_ext, sort_by):
    # data : 2차원 정수 리스트
    # ext : 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
    # val_ext : 뽑아낼 정보의 기준값
    # sort_by : 정보를 정렬할 기준이 되는 문자열
    ext_num = 0
    if ext == 'date':
        ext_num = 1
    elif ext == 'code':
        ext_num = 0
    elif ext == 'maximum':
        ext_num = 2
    elif ext == 'remain':
        ext_num = 3

    sort_by_num = 0
    if sort_by == 'date':
        sort_by_num = 1
    elif sort_by == 'code':
        sort_by_num = 0
    elif sort_by == 'maximum':
        sort_by_num = 2
    elif sort_by == 'remain':
        sort_by_num = 3

    new_data = []
    for d in data:
        if d[ext_num] < val_ext:
            new_data.append(d)

    print(new_data)
    new_data.sort(key=lambda x: x[sort_by_num])

    answer = new_data
    return answer