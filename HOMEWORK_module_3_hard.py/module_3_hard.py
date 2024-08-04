# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные,
# что иногда по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
# Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функци, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
#
# """
def calculate_structure_sum(*args):
    summa = 0
    for i in args:
        if isinstance(i, list):
            for k in i:
                summa += calculate_structure_sum(k)
        elif isinstance(i, tuple):
            for k in i:
                summa += calculate_structure_sum(k)
        elif isinstance(i, set):
            for k in i:
                summa += calculate_structure_sum(k)
        elif isinstance(i, dict):
            for key, value in i.items():
                summa += calculate_structure_sum(key, value)
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, int):
            summa += i
    return summa


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)