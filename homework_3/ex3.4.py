#4. Написать функцию square, принимающую 2 аргумента — длину сторон прямогольника, и возвращающую 3 значения:
#периметр, площадь и диагональ прямоугольника.
from math import *
def square(side1, side2):
    perimeter= 2*(side1+side2)
    area=side1*side2
    diagonal=sqrt(side1**2+side2**2)
    return(perimeter, area, diagonal)

side1 = 4
side2 = 3
print(square(side1, side2))