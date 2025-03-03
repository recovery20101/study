import json                                                                         #import json бібліотеки для більш зрозумілого виводу данних

def get_cats_info(path):                                                            #визначення функції
    try:
        with open(path, "r", encoding='utf-8') as data:                             #ввідкриття файлу
            cat_list = []
            for line in data:                                                       #цикл для перебору рядків у файлі
                result = line.strip().split(',')
                if len(result) == 3:                                                #перевірка на наявність 3 елементів  у рядку
                    cat_dict = {"id": result[0],
                                "name": result[1], 
                                "age": result[2]}  
                    cat_list.append(cat_dict)                          
        return cat_list       
        
    except FileNotFoundError:                                                       #перевірка на помилки
        print("Помилка: Файл не знайдено!")
        return []
    except UnicodeDecodeError:
        print("Помилка: Неможливо прочитати файл через неправильне кодування!")
        return []

directory_path = r"data.txt"                                                        #змінна для вказання директорії
cats_info = get_cats_info(directory_path)
print(json.dumps(cats_info, indent = 4, ensure_ascii=False))
        