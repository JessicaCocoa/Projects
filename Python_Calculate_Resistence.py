##Python program that calculates electrical resistance.
continue_program = input("Type n to exit or y to continue : ") #

while continue_program.lower() == "y": ##starts the program in a continous loop as long as they choose "y"
    print("Welcome to the Python program that calculates electrical resistence!")
    print ("-"*30)
    voltage = int(input("Please enter the voltage: "))
    current = int(input("Please enter the current: "))
    if current == 0:
        print("Current cannot be zero. Please enter a non-zero value for current.")
    elif continue_program.lower() =="y":
        resistance = voltage/current ##problem to calculate resistance
        print(f"The resistance is {resistance} \u03A9")
    else:
        print("you entered an invalid response") ##
    continue_program = input("Type n to exit or y to continue: ")  ##asks if they would like to continue
