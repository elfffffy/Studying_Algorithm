import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pocket_mon_dict_num = {}
pocket_mon_dict_name = {}
for i in range(1, N + 1):
    pocket_mon = input().strip()
    pocket_mon_dict_num[i] = pocket_mon
    pocket_mon_dict_name[pocket_mon] = i

for _ in range(M):
    question = input().strip()
    if question.isdigit():
        print(pocket_mon_dict_num[int(question)])
    else:
        print(pocket_mon_dict_name[question])
