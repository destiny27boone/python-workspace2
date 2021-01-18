'''
Created on Jan 18, 2021

The Objective is to make a program that can complete different conversions. 
The tasks to complete are:
Have the user input a number of miles.
Convert the number of miles to yards, feet, and inches.
Print out the conversions with a simple statement:

@author: Destiny Boone
'''
miles = 1 
yards = 1760

yards = miles * 1760
print(str(miles) + " mile converts to " + str(yards) + " yards.")

feet = miles * 5280
print(str(miles) + " mile converts to " + str(feet) + " feet.")


inches = miles * 63360
print(str(miles) + " mile converts to " + str(inches) + " inches.")