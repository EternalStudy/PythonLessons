'''
Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
3 -> 3.142
'''
from cmath import pi

N = int(input("Задайте количество знаков после запятой ПИ: "))
print(f"{pi:.{N+1}}")