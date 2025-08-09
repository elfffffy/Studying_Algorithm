# 상근이가 가지고 있는 숫자 카드의 개수
N = int(input())

# 카드에 적혀있는 정수, 중복 x
card_list = list(map(int, input().split()))

# 비교 대상 카드 개수
M = int(input())

# 비교 대상 카드
target_card = list(map(int, input().split()))

dat = [0] * 10000001 * 2

for card in card_list :
    if card < 0 :
        dat[abs(card) + 10000001] = 1
    else :
        dat[card] = 1

for target in target_card :
    if target < 0 :
        target = abs(target) + 10000001
    if dat[target] == 1 :
        print(1, end=" ")
    else:
        print(0, end=" ")
