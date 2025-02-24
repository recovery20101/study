import random

def get_numbers_ticket(min, max, quantity):                           # оголушуємо функцію
    try:
        min = int (min)                                               # оголушуємо змінні
        max = int (max)
        quantity = int (quantity)
        list_of_numbers = []
        if min < 1:                                                   # перевірка параметрів на валідність
            print ('Мінімальне число меньше 1')
            return print(f'{list_of_numbers}')
        if max > 1000:
            print ('Максимальне число більше 1000')
            return print(f'{list_of_numbers}')
        elif  min <= max and quantity <= max:                         # виконання основного блоку                     
            list_of_numbers = range(min, max + 1)
            output_numbers = random.sample(list_of_numbers, quantity)
            output_numbers.sort()
            return print(f"Команда: {output_numbers}")
        else:
            print ('Перевірте правильність данних')
    except ValueError:                                                # виконнаня блоку, якщо введене не число
        return print ('One of the value is not a number')

min = input("Введіть мінімальне число (не менше 1): ")                # ввод данних користувачем
max = input("Введіть максимальне число (не більше 1000): ")
quantity = input("Введіть кількість чисел, які потрібно вибрати (значення між min і max): ")      
get_numbers_ticket(min, max, quantity)                                # виклик функції