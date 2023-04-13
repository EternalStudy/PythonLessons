#5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений

lenght = int(input('Введите длинну списка: '))
array = []
for value in range(lenght):
    array.insert(value, int(input(f'Введите {value + 1}-e значение: ')))
print(f"Минимальное значение: {min(array)}")
print(f'Максимальное значение: {max(array)}')