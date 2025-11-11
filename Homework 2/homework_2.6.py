#6. “Периметр прямокутника”

#Користувач вводить довжину і ширину. Програма виводить периметр.

#Приклад:

#Введіть довжину: 5

#Введіть ширину: 3

#Периметр: 16

length = int(input("Please enter the length of your figure: "))
width = int(input("Please enter the width of your figure: "))
perimeter = (length + width) * 2
square = length * width
print(f"The perimeter of the figure is: {perimeter} and the square is: {square}.")