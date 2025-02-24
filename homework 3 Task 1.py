from datetime import datetime, timedelta

def get_days_from_today(date_string):                           # оголушуємо функцію
    try:                                                        # додаємо блок з перевіркою
        input_date = datetime.strptime(date_string, "%Y.%m.%d") # конвертуємо строку в задану дату
        current_date = datetime.today()                         # поточна дата
        difference = current_date - input_date                  # різниця дат
        return print(f"Difference is {difference.days} days")
    except ValueError:                                          # блок у випадку неккортного вводу дати
        return print ('The value is not a date')

input_date = input("Введіть дату у форматі YYYY.MM.DD: ")       # ввод дати користувачем
get_days_from_today(input_date)                                 # виклик функції