'''
Created on Nov 16, 2020

@author: Destiny Boone
'''

'''
This function takes a list of numbers of FIVE numbers and calculates the:
sum (all the numbers added up)
average (add all the numbers up and divide by how many there are)
range (biggest number - smallest number) (the biggest number is always the
last item and the smallest number is the first item)

'''
def calculations (list):
    print("The sum is:")
    sum = list[0] + list[1] + list[2] + list[3] + list[4] 
    print(sum)
    
    print("The average is:")
    average = sum / 5
    print(average) 
    
    print("The range is")
    diff = list[0] + list[4]
    print(diff)
    
    return

#Leave the following lines alone.
list = [24, 35, 46, 67, 78]
calculations(list)