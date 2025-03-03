def total_salary(path):                                                             #визначення функції
    try:
        with open(path, "r", encoding='utf-8') as data:                             #ввідкриття файлу
            salary_list=[]
            for line in data:                                                       #цикл для перебору рядків у файлі
                result = line.split(',')
                for num in result:
                    clean_num = num.strip()  
                    if clean_num.isdigit():                                         #перевірка чи є значення числом і запис у salary_list
                        salary_list.append(int(clean_num))                          
        
        if not salary_list:                                                         #перевірка, якщо у заданому файлі немає чисел
            return {
                "total": 0, 
                "average": 0
                }
        
        total_sal = sum(salary_list)                                                #розрахунок значень
        avg_sal = sum(salary_list) / len(salary_list)
        return (total_sal,avg_sal)                                                  #повернення кортежу
        
    except FileNotFoundError:                                                       #перевірка на помилки
        print("Помилка: Файл не знайдено!")
        return None
    except UnicodeDecodeError:
        print("Помилка: Неможливо прочитати файл через неправильне кодування!")
        return None

directory_path = r"data.txt"  #змінна для вказання директорії
total,average = total_salary(directory_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

        