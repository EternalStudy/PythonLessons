# Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
import random

def indexes(num: list):
    indexes = [i for i in range(len(num))]      
    result = [] 
    while len(indexes) > 0:  
        index = indexes.pop(random.randint(0, len(indexes)-1))             

        if len(result) == 0 or num[index] > result[-1]:
            result.append(num[index])
        else:
            return result    
    
def lIst():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num), indexes(num)

def sort(num):
    flag = True
    while flag:
        result = indexes(num)
        if len(result) > 1:
            print(f'Случайная возрастающая последовательность: {result}')
            flag = False
    
lIst()
