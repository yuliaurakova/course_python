# 4)Пользователь вводит три числа. Написать "yes", если можно взять какие-то два из них и в сумме получить третье
l = [int(input()), int(input()), int(input())]
l.sort()
if l[0] + l[1] == l[2]:
    print('yes')
else:
    print('no')