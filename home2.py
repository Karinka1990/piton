#Найдите произведение элементов списка с нечетными номерами

from math import prod
A = [3, 2, 5, 7, 4, 9]
for i in range(len(A)):
    if A[i]%2 == 0 in A:
        A.remove(A[i]%2 == 0)
        print(A)





#Найдите наибольший элемент списка, затем удалите его и выведите новый список
A = [3, 2, 5, 7, 4, 9]
max =  A[0]
for i in range(1, len(A)):
    if A[i]> max:
        max= A[i]
print(max)
A.remove(max)
print(A)