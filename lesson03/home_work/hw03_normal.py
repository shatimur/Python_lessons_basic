# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_1 = 1
    fib_2 = 1
    fib_lst = [1,1] # лист, в который мы будем добавлять остальные числа Фибоначчи

    i = 0

    while i < m - 2:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        i = i + 1
        fib_lst.append(fib_2)

    return fib_lst[n:m]

print(fibonacci(6, 9))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

def sort_to_max(origin_list):
        a = origin_list             # для сокращения записи индексов вводим временную переменную
        for j in range(0, len(a)-1):
            for i in range(0, len(a)-1-j):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
        return origin_list

print(sort_to_max(origin_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

seq = []
def my_filter(func, seq):
    filtered_lst = []
    for itm in seq:
        if func(itm):
            filtered_lst.append(itm)
    return filtered_lst

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parall(x1, y1, x2, y2, x3, y3, x4, y4):
    if abs(x1-x2) == abs(x3-x4) and abs(y1-y2) == abs(y3-y4):
        print("Это вершины параллелограмма")
    else:
        print("Эти вершины не образуют параллелограмм")
