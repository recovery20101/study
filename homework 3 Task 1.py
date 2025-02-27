from datetime import datetime, timedelta

def get_days_from_today(date_string):                                   # оголушуємо функцію
    try:                                                                # додаємо блок з перевіркою
        input_date = datetime.strptime(date_string, "%Y-%m-%d")  # конвертуємо строку в задану дату
        current_date = datetime.today()                         # поточна дата
        difference = current_date - input_date                          # різниця дат
        return difference.days
    except ValueError:                                                  # блок у випадку неккортного вводу дати
        print ('The value is not a date')
        return None

input_date = input("Введіть дату у форматі YYYY-MM-DD: ")               # ввод дати користувачем
print(get_days_from_today(input_date))                                  # виклик функції