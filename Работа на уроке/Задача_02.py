#Организуйте последовательный ввод чисел до тех
#пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

number=1
while number!=0:
    number= float(input('Number? '))
    print(number%3==0)
print('End!')
