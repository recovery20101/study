import sys                                                                          #імпортуємо необхідні бібліотеки
from pathlib import Path
from colorama import Fore

def dir_structure(dir,prefix =""):                                                  #оголушуємо функцію обробки структури
    entries = sorted(dir.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))    #сортуємо файли по назві та типу(папка чи файл)
    for path in entries:
        if path.is_dir():                                                           #перевірка чи це шлях директорії
            print(f"{prefix}{Fore.BLUE}{path.name}/ {Fore.RESET}")                  
            dir_structure(path, prefix + "    ")                                    #рекурсивний виклик функції
        else:                                                                       #перевірка чи це шлях файлу
            print(f"{prefix}{Fore.GREEN}{path.name} {Fore.RESET}")



if __name__ == "__main__":                                                         
    directory = Path(sys.argv[1])                                                    #запис файлу в змінну
    if not directory.exists() or not directory.is_dir():                             #перевірка чи існує директорія
        print("Error: Invalid directory path")
        sys.exit(1)   
    dir_structure(directory)

