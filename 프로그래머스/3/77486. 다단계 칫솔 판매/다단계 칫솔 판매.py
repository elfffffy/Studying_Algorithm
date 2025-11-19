from collections import defaultdict


def calculate(p):
    my_p, rest_p = 0, 0
    if p * 0.1 < 1:
        my_p = p
    else:
        rest_p = int(p * 0.1)
        my_p = p - rest_p

    return my_p, rest_p


def solution(enroll, referral, seller, amount):
    graph = defaultdict(str)
    money = defaultdict()

    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
        money[enroll[i]] = 0

    for j in range(len(seller)):
        person = seller[j]
        profit = amount[j] * 100

        while True:
            my_profit, rest_profit = calculate(profit)
            if person == "-": break
            money[person] += my_profit
            if person == '-': break
            if rest_profit == 0 or my_profit == profit: break
            profit = rest_profit
            person = graph[person]

    answer = []
    for name in enroll:
        answer.append(money[name])
    return answer