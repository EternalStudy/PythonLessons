import numpy as np
def task2():
    size = 10
    numbers = np.random.randint(10, 100, size)
    print(numbers)

    mean = np.mean(numbers)
    print(f'среднее арифметическое {mean}')

    
    num = int(input('\nВведите число: '))
    dist = [np.abs(el - num) for el in numbers]
    print(f'дистанции {dist}')
    min_dist = np.min(dist)
    print(f'минимальное расстояние {min_dist}')
    index_min_dist = dist.index(min_dist)
    print(f'индекс минимального расстояния {index_min_dist}')

    print(f'ближайший элемент к {num} равен {numbers[index_min_dist]}')

task2()