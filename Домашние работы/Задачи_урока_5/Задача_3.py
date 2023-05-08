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
    return print(num), sort(num), count(num)

def sort(num):
    arr = list(dict.fromkeys(num))
    print(arr)
    newElement = set(arr)
    print(f'Совпадающих элементов в numbers: {len(num) - len(newElement)}')
    print(f'Множество уникальных элементов: {newElement}')

def count(num):
    counter = {}
    for Elem in num:
        counter[Elem] = counter.get(Elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    print(doubles)
lIst()

