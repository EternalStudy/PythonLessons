#Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy
import random

def method():
    two_dimensional_array = numpy.random.randint(2, size=(5, 5))
    unique_rows = numpy.unique(two_dimensional_array, axis=0)
    print(two_dimensional_array)
    if unique_rows.shape[0] < two_dimensional_array.shape[0]:
        print("В двумерном массиве есть одинаковые строки")
    else: 
        print("Одинаковых строк нет")