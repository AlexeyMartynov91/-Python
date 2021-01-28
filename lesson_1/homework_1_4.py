'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
'''

text = input("Вводите целое положительное число: ")
value = int(text)
min = 9
max = 0
while value > 0:
    v = value % 10
    value = value // 10
    if v > max:
        max = v
    if v < min:
        min = v
print(f"Максимальное число в строке {text}: {max}")
print(f"Минимальное число в строке {text}: {min}")
