
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
'''
def is_true_statement(x, y, z):
    if not(x or y or z) == (not x and not y and not z):
        return 1
    else:                                                         # функция возврата истинности утверждения
        return 0


ijk_list = []                                                     # список истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 

for i in range(2):
    for j in range(2):                                            # циклы для создания всех возможных значений x y z
        for k in range(2):
            ijk_true_false = is_true_statement(i, j, k)           # переменная в которую кладем инстиность утверждения с значениями конкретной итерации 0 0 0, 0 0 1, 0 1 0... и передаем в цункцию на проверку 
            ijk_list.append(ijk_true_false)                       # заполняем список

print(ijk_list)                                                   # я так понял, что всегда истинно
'''


ijk_list = [1 for i in range(2) for j in range(2) for k in range(2) if (lambda i, j, k: not(i or j or k) == (not i and not j and not k))]     #нули не выведет, но их не может быть а если 8 единиц значит все 8 верные
print(ijk_list)