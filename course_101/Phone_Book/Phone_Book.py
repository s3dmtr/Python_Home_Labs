phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed ",
    "3333333333": "Khadijah ",
    "4444444444": "Abdullah ",
    "5555555555": "Rawan ",
    "6666666666": "Faisal ",
    "7777777777": "Layla ",
}


def find_by_number(number):
    if len(number) != 10 or not number.isdigit():
       print("This is not a valid number")
    
    elif number not in phone_book:
        print("Number not found")
        
    else:
            print(phone_book[number])


def find_by_name(name):
    for number in phone_book:
        if phone_book[number].lower() == name.lower():
            print(number)
            return
    print("Name not found")


def add_contact(name, number):
    if len(number) != 10 or not number.isdigit():
        print("Cannot add: Invalid number format.")
        
    else:
        phone_book[number] = name
        print(f"Successfully added {name}!")


find_by_name("Amal")
find_by_number("1111111111")
add_contact("Sara", "8888888888")
