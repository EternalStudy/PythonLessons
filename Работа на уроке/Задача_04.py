#4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
num = input("Введите число: ")
if type(num) == float:
    print(f"{num} -> {int(num*10%10)}")
else:
    print(f"{num} -> нет")