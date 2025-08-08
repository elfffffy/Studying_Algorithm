text = input()
dat = [0] * 26

for char in text:
    dat[ord(char) - 97] += 1

print(*dat)
