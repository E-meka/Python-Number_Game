#Tries to beat the robot's number between 1 and 100"#
import random
import sys

number = (random.randrange(1,100))
user_ask = int(input("Enter a number between 1 and 100. "))

if user_ask > 100:
print("The input was larger than the parameters please try again!")
sys.exit()

if user_ask < 1:
    print("The input was smaller than the parameters please try again!")
sys.exit()

if user_ask < number:
    print("The robot has the larger number. \nThe number was: "+str(number))

if user_ask > number:
    print("You have beaten the robots number! \nThe number was: "+str(number))

#if user_ask == number:
    print("You and the robot have tied, there is no winner. \nThe number was : "+str(number))

print("Your entered number was: " + str(user_ask))