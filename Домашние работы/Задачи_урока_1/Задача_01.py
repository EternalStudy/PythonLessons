""""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
1 –> Понедельник
10 –> Нет такого дня
7 –> Воскресение
"""


def Method_One():
    num_day = int(input('Введите номер дня недели '))
    if num_day == 1:
        print('Понедельник')
    elif num_day == 2:
        print('Вторник')
    elif num_day == 3:
        print('Среда')
    elif num_day == 4:
        print('Четверг')
    elif num_day == 5:
        print('Пятницы')
    elif num_day == 6:
        print('Суббота')
    elif num_day == 7:
        print('Воскресенье')

def Method_Two():
    num_day = int(input('Введите номер дня недели '))
    days_week = ['Понедельник',
                 'Вторник',
                 'Среда',
                 'Четверг',
                 'Пятница',
                 'Суббота',
                 'Воскресанье']
    for i in days_week:
        if num_day-1 >=0 and num_day -1 < 7:
            print(days_week[num_day -1])
            break
        else:
            print('Введенный день недели - неверный. Повторите ввод.')
