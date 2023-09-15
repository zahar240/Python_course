"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""


number = 5
factorial = 1

while number > 1:
    factorial *= number
    number -= 1
print(factorial) 


"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

number = 13
fib_penultimate, fib_last = 0, 1
count = 2
while number > fib_last:
    fib_penultimate, fib_last = fib_last, fib_penultimate + fib_last
    count += 1
if number == fib_last:
    print(count)
else:
    print("-1")


"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе. 
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""


days = int(input('Введите общее количество рассматриваемых дней: '))
temperature = [int(x) for x in input('Введите среднесуточные температуры в рассматриваемые дни через пробел: ').split()]
count_plus = 0
count_count = 0
for el in temperature:
    if el > 0:
        count_plus += 1
    elif el <= 0:
        count_plus = 0
    if count_plus > count_count:
        count_count = count_plus
print(count_count)

# Второй вариант
from random import randint

amount_days = int(input("Введите количество рассматриваемых дней: "))
temps = []

for i in range(amount_days):
    temps.append(randint(-50, 50))
count_max_warm, count = 0, 0
for i in temps:
    if i > 0:
        count += 1
    else:
        if count_max_warm < count:
            count_max_warm = count
            count = 0
print(temps)
print(count_max_warm)


"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""