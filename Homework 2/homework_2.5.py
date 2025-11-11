#5. “Остання цифра числа”

#Користувач вводить ціле число, програма виводить його останню цифру.

#Приклад:

#Введіть число: 347

#Остання цифра: 7

number = int(input("Please enter a number: "))
last_digit = number - (number // 10) * 10
print("Last digit is:", last_digit)