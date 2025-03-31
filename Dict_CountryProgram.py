def display_menu():
    print("view - view country name")
    print("add - add a country")
    print("del - Delete a country")
    print("exit - exit the program")
    print()


def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    code_lines = "Country codes: "
    for code in codes:
        print(code)

def view(countries):
    display_codes(countries)
    code = input ("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}")
    else:
        print("There is no country with that code")

def add(countries):
    code = input ("enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print (f"{name} is already using that code")
    else:
        name = input ("Enter country name")
        name = name.title() ##put it in title case
        countries[code] = name ## assigns it to the value
        print(f"{name} was added")

def delete(countries):
    code = input("Enter country code")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted!")
    else:
        print("There is no country with that code")

def main():
    countries = {"CA":"Canada", "US":"United States", "MX":"Mexico"}

    display_menu()
    while True:
        command = input("Command :  ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command == "exit":
            print ("Bye")
            break
        else:
            print("not a valid command. Please try again!")

if __name__=="__main__":
    main()


