T = int(input())

for tc in range(1, T + 1):

    N = int(input())  # N 카드 장수
    cards = input()  # 카드
    max_cnt = 0
    max_num = 0

    for i in range(10):
        cnt = cards.count(str(i))
        if cnt >= max_cnt:
            max_cnt = cnt
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')