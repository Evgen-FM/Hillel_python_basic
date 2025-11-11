#2. “Середнє трьох чисел”
from sys import api_version

#Програма запитує три числа і виводить їх середнє арифметичне.

#Приклад:

#Введіть три числа: 2, 4, 6

#Середнє: 4.0

num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")
num3 = input("Please enter third number: ")
average = (float(num1) + float(num2) + float(num3)) / 3
print("The average is: ", average)