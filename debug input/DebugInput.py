'''
The goal of this function is to calculate the 
area of a circle.

The function gets a radius from the user and 
then calculates the area.

The function should print and
return the area.
'''
def circleArea():
    radius = input("What is the radius of your circle?")
    
    pi = 3.14
    squared = radius * radius
    area = pi * squared 
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea()



'''
This function calculates the area of a rectangle.

The function gets a height and width from the user and then calculates
the area.

The function prints and returns the area.
'''
def rectangleArea():
    height = input("What is the height of your rectangle?")
    width = input()
    
    area = height * width
    print("The area is:" + area)
    return area

#Leave the next line alone
rectangleArea()