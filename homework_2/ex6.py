# 6) Пользователь вводит строку. Напечатать словарь, ключами которого являются четные символы строки,
#  а значениями нечетные. Если значению не хватает ключа, не добавлять его в словарь.
str = str(input())
key=str[1::2]
print(key)
value=str[::2]
print(value)
dict={}
i=0
while i< len(key):
    dict[key[i]]=value[i]
    i += 1
else:
    print (dict)