
__author__ = 'Сериков Павел Евгеньевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

	num_new = number * 10 ** ndigits

	if num_new - int(num_new) >= 0.5:
		num_new += 1

	number = int(num_new) / (10 ** ndigits)

	return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.9999937, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	len_half = len(str(ticket_number)) // 2
	# на случай, если длина билета нечетная (среднюю цифру учитывать не будем)
	len_odd = len(str(ticket_number)) % 2 

	begin_sum = 0
	end_sum = 0

	for i in range(0, len_half):
		begin_sum += int(str(ticket_number)[i])

	for i in range(len_half + len_odd, len(str(ticket_number))):
		end_sum += int(str(ticket_number)[i])

	if begin_sum == end_sum:
		return "Билет счастливый!!!"
	else:
		return "Билет несчастливый (("


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))