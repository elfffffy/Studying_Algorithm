def check_vowels(lst):
    vowels_cnt = 0
    consonant_cnt = 0

    for letter in lst:
        if letter in vowels:
            vowels_cnt += 1
        else:
            consonant_cnt += 1

    if vowels_cnt >= 1 and consonant_cnt >= 2:
        return True
    else:
        return False


def func(lev, start):
    if lev == l:
        if not check_vowels(path): return
        path.sort()
        print(''.join(path))
        return

    for i in range(start, c):
        path.append(letters[i])
        func(lev + 1, i + 1)
        path.pop()


l, c = map(int, input().split())  # l: 알파벳 개수, c: 문자의 종류
vowels = ['a', 'e', 'i', 'o', 'u']
letters = list(input().split())
letters.sort()
path = []
func(0, 0)
