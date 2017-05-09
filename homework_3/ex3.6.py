# 6. Написать функцию-фабрику, которая будет возвращать функцию умножения на аргумент
# Пример:
# mult5 = multiple_inner(5)
# print(mult5(7))
# 35

def newfunc(n):
    def myfunc(x):
        return x * n
    return myfunc

new = newfunc(400)
fun_fabr = new(2)

print(fun_fabr)
