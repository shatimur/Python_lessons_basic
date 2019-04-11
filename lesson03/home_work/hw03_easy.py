# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number_round = int(number * 10**5)/(10**5)
    last_digit = str(number_round)[-1]
    if int(last_digit) >= 5:
        number_round += 0.00001
    return number_round


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

### В условии задачи следует уточнить, каких именно первых и последних цифр.

def lucky_ticket(ticket_number):
    half1 = str(ticket_number)[:3]
    half2 = str(ticket_number)[3:]
    a = map(int, half1)
    b = map(int, half2)
    sum1 = sum(a)
    sum2 = sum(b)
    if sum1 == sum2:
        return 'Билет счастливый'
    else:
        return 'Билет не счастливый'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
