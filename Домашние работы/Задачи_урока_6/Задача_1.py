# Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

def chislo(N: int):
    return N + int(str(N) + str(N)) + int(str(N) + str(N) + str(N))

N = int(input('Введите число '))
N=abs(N)
print(f'Результат для N={N}: {chislo(N)}')
