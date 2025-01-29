
# Celsius to Fahrenheit AND Fahrenheit to Celsius Converter
continue_program = input("Enter y to continue or n to stop: ")

while continue_program.lower() == "y": ##allows for user to give choice in which conversion they are using
    choice = input("Enter c to get the temperature in Celsius or f to get the temperature in Fahrenheit: ")
    if choice.lower() == "c": ##Celsius conversion
        f_cel = float(input("What is the degree in Fahrenheit you would like to convert to Celsius? "))
        answer = int(5 / 9 * (f_cel - 32))
        print(f"{f_cel} Fahrenheit is {answer} Celsius")
    elif choice.lower() == "f": ## Fahrenheit conversion
        c_fah = float(input("What is the degree in Celsius you would like to convert to Fahrenheit? "))
        answer = (9 * c_fah) / 5 + 32
        print(f"{c_fah} Celsius is {answer} Fahrenheit")
    else: ## if user put an invalid entry
        print("You entered an invalid entry.")

    continue_program = input("Enter y to continue or n to stop: ")
