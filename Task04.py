# Task 4: Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
def list (n):
    list = []
    for i in range(n):
        list.append(randint(-n,n))
        return list
n = int (input('Введите число N: '))    
num = list(n)
print(num)
x = open('file.txt', 'r')
result = num [int(x.readline())] * num[int(x.readline)(2)]
print(result)    
