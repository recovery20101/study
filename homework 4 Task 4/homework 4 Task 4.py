def parse_input(user_input):                                                #функція для парсінгу команд
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.lower() for arg in args]
    return cmd, *args

def add_contact(args, contacts):                                            #функція для додавання контактів, обробка помилок
    try:
        name, phone = args
        if name in contacts:
            return "Contact already exists."
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError:
        return "Error: Invalid input format. Use 'add <name> <phone>'."

def change_contact(args, contacts):                                         #функція для зміни контактів, обробка помилок
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact is missing."
    except ValueError:
        return "Error: Invalid input format. Use 'change <name> <phone>'."
    
def show_phone(args, contacts):                                             #функція для виводу телефону, обробка помилок
    try:
        return contacts.get(args[0], "Contact is missing.")
    except IndexError:
        return "Error: Missing name. Use 'phone <name>'."
    
def all(contacts):                                                          #функція для повернення списку контактів
    return contacts

def main():                                                                 #мейн функція 
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:                                    #виклик функцій в залежності від команди
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()