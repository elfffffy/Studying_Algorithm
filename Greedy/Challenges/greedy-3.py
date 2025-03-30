s = input()
group_zero = 0
group_one = 0

for i in range(len(s)):

    if i != len(s) - 1:

        if s[i] != s[i + 1]:

            if s[i] == "0":
                group_zero += 1

            else:
                group_one += 1

print(min(group_zero, group_one))
