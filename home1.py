#Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
import numpy as np
m=-2
n=5
p=-10
mas = [m, n, p]
I = len(mas)
for i  in range(I):
    if mas[i]<0:
        print(mas[i])



#Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.
a=3
b=7
c=3
print(a==b)
print(a==c)
print(b==c)

#Даны три числа a, b и c. Найти среднее среднее арифметическое
a=3
b=7
c=5
A=[a,b,c]
s=sum(A)
I=len(A)
y=s/I
print(y)
a=p**(1/I)
print(a)

