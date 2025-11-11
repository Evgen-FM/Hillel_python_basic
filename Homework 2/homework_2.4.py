#4. “Розрахунок знижки”

#Користувач вводить ціну товару і розмір знижки у %.

#Програма виводить кінцеву ціну.

#Приклад:

#Введіть ціну: 1000

#Введіть знижку (%): 15

#Ціна зі знижкою: 850.0

price = float(input("Enter price: "))
discount = float(input("Enter discount(%): "))

print(f"The current price is {price - price * discount / 100}")
