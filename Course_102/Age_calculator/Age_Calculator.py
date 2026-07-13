#--------------------
#\\//\\//\\//\\//\\//
#|||| Importing |||||
#\\//\\//\\//\\//\\//
#--------------------
import datetime

#---------------
#\\//\\//\\//\\
#|||| Date |||||
#\\//\\//\\//\\
#---------------
import datetime
time = datetime.date(2021, 1, 1)

#---------------------
#\\//\\//\\//\\//\\//
#|||| Dectionary |||||
#\\//\\//\\//\\//\\//
#---------------------

people ={
        
}


#--------------------
#\\//\\//\\//\\//\\//
#|||| Functions |||||
#\\//\\//\\//\\//\\//
#--------------------





# -----------------------------
# Validate Date
# -----------------------------
def validate_date(date_of_birth):

    parts = date_of_birth.split("-")

    if len(parts) != 3:
        return None

    if not all(part.isdigit() for part in parts):
        return None

    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])

    try:
        birth_date = datetime.date(year, month, day)
        return birth_date

    except ValueError:
        return None


# -----------------------------
# Calculate Age
# -----------------------------
def calculate_age(birth_date):

    age = time.year - birth_date.year

    if birth_date.month > time.month:
        age -= 1

    elif birth_date.month == time.month and birth_date.day > time.day:
        age -= 1

    return age


# -----------------------------
# Day Name
# -----------------------------
def get_day_name(birth_date):

    return birth_date.strftime("%A")


# -----------------------------
# Print Person
# -----------------------------
def print_person(name, birth_date):

    age = calculate_age(birth_date)
    day = get_day_name(birth_date)

    print(f"{name} is {age} years old and she/he was born on {day}")


# -----------------------------
# Oldest Person
# -----------------------------
def find_oldest():

    return min(people, key=people.get)


# -----------------------------
# Youngest Person
# -----------------------------
def find_youngest():

    return max(people, key=people.get)


# -----------------------------
# Sort People
# -----------------------------
def sort_people():

    print("\nPeople from oldest to youngest:")

    sorted_people = sorted(people.items(), key=lambda person: person[1])

    for name, birth_date in sorted_people:
        print(name)


# -----------------------------
# Reverse Input
# -----------------------------
def reverse_people():

    print("\nReverse order:")

    reversed_people = list(people.items())

    reversed_people.reverse()

    for name, birth_date in reversed_people:
        print(name)


# -----------------------------
# Sunday People
# -----------------------------
def sunday_people():

    print("\nPeople born on Sunday:")

    found = False

    for name, birth_date in people.items():

        if get_day_name(birth_date) == "Sunday":
            print(name)
            found = True

    if not found:
        print("No one was born on Sunday.")


# -----------------------------
# Main Function
# -----------------------------
def names_ages():

    choice = input("Do you want to enter a person? (Y/N): ").upper()

    while choice != "N":

        if choice == "Y":

            name = input("Enter name: ").title()

            date_of_birth = input("Enter date of birth (DD-MM-YYYY): ")

            birth_date = validate_date(date_of_birth)

            if birth_date:
                people[name] = birth_date

            else:
                print(f"Invalid date: {name}")

        else:
            print("Invalid choice.")

        choice = input("Do you want to enter another person? (Y/N): ").upper()

    print()

    for name, birth_date in people.items():
        print_person(name, birth_date)

    print()

    if len(people) > 1:
        print(f"The oldest one is {find_oldest()}")
        print(f"The youngest one is {find_youngest()}")
    else:
        print("There is no oldest or youngest person.")

    print(f"Total People: {len(people)}")

    print()

    sort_people()

    reverse_people()

    sunday_people()


names_ages()
