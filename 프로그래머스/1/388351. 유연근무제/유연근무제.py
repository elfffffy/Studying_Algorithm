def solution(schedules, timelogs, startday):
    admin_schedules = []

    for schedule in schedules:
        time = schedule + 10

        if time % 100 > 59:
            time = time + 100 - 60

        admin_schedules.append(time)

    person = 0
    day = startday
    answer = 0

    for timelog in timelogs:
        is_pass = True
        deadline = admin_schedules[person]

        for time in timelog:
            if day > 7:
                day = day % 7
                if day == 0:
                    day = 7

            if day == 6 or day == 7:
                day += 1
                continue

            if time > deadline:
                is_pass = False
                break

            day += 1

        if is_pass:
            answer += 1

        person += 1
        day = startday

    return answer
