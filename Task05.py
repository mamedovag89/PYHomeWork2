# Task 5: Реализуйте алгоритм перемешивания списка.
import random

n = int(input("Введите длину списка: "))

list = []

for i in range(n):
    list.append(random.randint(0, n + 7))
    
print(list)

def peremesh(list):
  for i in range (len(list)):
    random_n = random(0, n-1)
    temp = list[i]
    list[i] = list[random_n]
    list[random_n] = temp

print(list)