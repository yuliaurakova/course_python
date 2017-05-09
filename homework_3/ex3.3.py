#3. Написать функцию arithmetic, принимающую 3 аргумента:
#первые 2 - числа, третий - операция, которая должна быть произведена над ними.
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(number1, number2, оperation):
    if оperation == '+':
        number3=number1 + number2
    elif оperation == '-':
        number3 = number1 - number2
    elif оperation == '*':
        number3 = number1 * number2
    elif оperation == '/':
        number3 = number1 / number2
    else:
        number3='Неизвестная операция'
    return number3

number1 = 2
number2 = 2
оperation = '/'

print(arithmetic(number1, number2, оperation))
