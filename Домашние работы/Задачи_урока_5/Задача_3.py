# Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random
def lIst():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num)

def sort(num):
    arr = list(dict.fromkeys(num))
    print(arr)
lIst()