s = input()
result = ''
calculater = ''

for i in s :
    if i == "0" :
        calculater = "+"
    elif i == s[-1] :
        calculater = ""
    else :
        calculater = "*"
    result += f"{i} {calculater} "

result = int(eval(result))

print(result)




