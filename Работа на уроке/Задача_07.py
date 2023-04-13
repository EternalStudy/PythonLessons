# Выведите таблицу истинности для выражения ¬ X ∨ Y.

#for i in range(2):
 #   for j in range(2):
  #      print(f"{i}\t{j}\t{bool( not i and j) }")
print(f'x | y | ¬ X ∨ Y')
for x in range(0, 2):
        for y in range(0, 2):    
            print(f'{x} | {y} | {int(not x or y)}')