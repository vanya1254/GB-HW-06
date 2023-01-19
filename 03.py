#  Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;


data = '1+2*3'
data = data.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
data_list = data.split()
print(data_list)

operation = {
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y),
    '*': lambda x, y: int(x)*int(y),
    '/': lambda x, y: int(x)/int(y)
}

def calc(data):
    for i in range(len(data) - 1):
        if data[i] in '*/':
            left = data[i - 1]
            right = data[i + 1]
            oper = data[i]
            res = operation[oper](left, right)
            return data[:i - 1] + res + data[i + 1:]
        
# while len(data_list) > 1: