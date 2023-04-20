#Создайте кортеж, заполненный случайными числами.
#Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.
def one():
    from random import randint


    def tupleAssign(tup, idx, value):
        tup = tup[:idx] + (value,) + tup[idx + 1:]
        return tup


    myTuple = tuple(randint(0, 9) for it in range(10))
    print(myTuple)
    myTuple = tupleAssign(myTuple, 2, "new")
    print(myTuple)

def TWO():
    import random
    def change_element(numbers, index):
        return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

    numbers = tuple(random.randint(1, 100) for _ in range(10))
    index = 2

    print(numbers)
    numbers = change_element(numbers, index)
    print(numbers)
    print(type(numbers))