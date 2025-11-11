#3. “Перетворення хвилин у години”

#Користувач вводить кількість хвилин. Програма виводить, скільки це годин і хвилин.

#Приклад:

#Введіть кількість хвилин: 135

#2 години 15 хвилин


minutes = int(input("Please enter quantity of minutes: "))
hours = minutes // 60
minute = minutes % 60
print(f"It is {hours} hours and {minute} minutes.")
