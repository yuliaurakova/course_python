# 5)Пользователь вводит число N. Создать массив размера N, который одинаково читается как слева направо,
# так и справа налево.
n=int(input())
s=n//2
if n%2==1:
    a = [i for i in range(1, s+2)]
    b = [i for i in range(s,0,-1)]
    print(a+b)
else:
    a = [i for i in range(1, s+1)]
    b = [i for i in range(s,0,-1)]
    print(a+b)