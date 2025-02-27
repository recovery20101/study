import random

def get_numbers_ticket(min, max, quantity):                                   # оголушуємо функцію
    try:
        min = int(min)                                                        # оголушуємо змінні
        max = int(max)
        quantity = int(quantity)
        list_of_numbers = []
        if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):  # перевірка параметрів на валідність
            return []
                           
        list_of_numbers = range(min, max + 1)
        output_numbers = random.sample(list_of_numbers, quantity)
        output_numbers.sort()
        return output_numbers
        
    except ValueError:                                                         # виконнаня блоку, якщо введене не число
        print ('One of the value is not a number')
        return []

min = input("Введіть мінімальне число (не менше 1): ")                # ввод данних користувачем
max = input("Введіть максимальне число (не більше 1000): ")
quantity = input("Введіть кількість чисел, які потрібно вибрати (значення між min і max): ")      
result = get_numbers_ticket(min, max, quantity)                       # виклик функції
print(result)