'''
Created on Feb 17, 2021

@author: Destiny Boone 
'''

correctAns = 0

print("1) What is the power house of the cell?")
ansOne = input("ENTER A LETTER: A) mitochondria B) nucleous C) ribosome")


if(ansOne.upper() == "A"):
    correctAns = correctAns + 1
    print("Correct!")
else:
    print("Incorrect, the correct answer is A.")


print("2) How many states comprise the United States?")
ansTwo = input("ENTER A LETTER: A) 13 B) 45 C) 50")


if(ansTwo.upper() == "C"):
    correctAns = correctAns + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")


print("3) In y = mx + b, what does m stand for?")
ansThree = input("A) slope B) output C) I don't understand math")


if(ansThree.upper() == "A"):
    correctAns = correctAns + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A")


print("4) In English, a person, place or thing is called:")
ansFour = input("A) verb B) adjective C) noun")


if(ansFour.upper() == "C"):
    correctAns = correctAns + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C")


p = correctAns / 4


print("You got a " + str(correctAns) + "/4. Or a " + str(p) + "%")


