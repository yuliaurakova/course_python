# 1. Написать функцию принимающую на вход число и возвращающую последовательность чисел Фибоначи до этого
#  числа.


def fibonachi_sequence(num):
    if num == 0:
        return []
    elif num == 1:
        return [0]
    pre_previous_number = 0
    previous_number = 1
    result_array = [0, 1]
    next_number = pre_previous_number + previous_number
    while next_number < num:
        result_array.append(next_number)
        pre_previous_number = previous_number
        previous_number = next_number
        next_number = pre_previous_number + previous_number
    return result_array


print(fibonachi_sequence(8))
