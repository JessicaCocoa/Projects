import math

##program to find Perimeter and Area of a given shape

print ("Hello, lets find the Perimeter and Area of a shape!")
##asks for customer input for type of shape

print ("To find the Area and Perimeter of a Square, press 1 : ")
print ("To find the Area and Perimeter of a Pentagon, press 2 : ")
print ("To find the Area and Perimeter of a Hexagon, press 3 : ")
print ("To find the Area and Perimeter of a Heptagon, press 4 : ")
print ("To find the Area and Perimeter of a Octagon, press 5 : ")
num_choice = int(input("number : "))


## - Square : Finding Permieter and Area
if num_choice == 1:
    side_Square = int(input("Input side length of square?"))
    perimeter_Square = side_Square * 4
    area_Square = side_Square**2
    print (f"Perimeter of square : {perimeter_Square}")
    print (f"Area of square : {area_Square}")


## Pentagon : Finding Perimeter and Area
elif num_choice == 2:
    side_Pentagon = int(input("Input the side length of the Pentagon?"))
    perimeter_Pentagon= side_Pentagon * 5
    area_Pentagon = (5 / 4) * side_Pentagon**2 * (1 / math.tan(math.pi / 5))
    print(f"Perimeter of Pentagon is : {perimeter_Pentagon}")
    print (f"Area of a Pentagon is : {area_Pentagon}")


## Hexagon : Finding Perimeter and Area
elif num_choice == 3:
    side_Hexagon = int(input("What is the side of Length Hexagon?"))
    perimeter_Hexagon = 6 * side_Hexagon
    a_Hexagon =  side_Hexagon**2 ##side of problem
    squareR_Hexagon = (math.sqrt(3) *3) /2
    area_Hexagon = squareR_Hexagon * a_Hexagon
    print (f"Perimeter of Hexagon : {perimeter_Hexagon}")
    print (f"Area of Hexagon : {area_Hexagon}")

## Heptagon : Finding Perimeter and Area
elif num_choice == 4:
    side_Heptagon = int(input("What is the side length of the Heptagon?"))
    perimeter_Heptagon = side_Heptagon * 7
    area_Heptagon = (7 * side_Heptagon**2) / (4 * math.tan(math.pi / 7))
    print(f"The Perimeter of the Heptagon is: {perimeter_Heptagon}")
    print(f"The Area of the Heptagon is: {area_Heptagon}")


#Octagon : Finding the Perimeter and Area
elif num_choice == 5:
    side_Octagon = int(input("What is the side length of the Octagon?"))
    perimeter_Octagon =  8 * side_Octagon
    area_Octagon = 2 * (1 + math.sqrt(2)) * side_Octagon ** 2
    print(f"The Perimeter of the Octagon is: {perimeter_Octagon}")
    print(f"The Area of the Octagon is: {area_Octagon}")

## Lets customer know they made an invalid selection
else:
    print("You did not enter a number that was 1-5. Please try again")


