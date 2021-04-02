import random
welcome = """
************************************************************
*                                                          *
*        Welcome to the Random Number Game!                *
*                                                          *
************************************************************
"""
print(welcome)
n = random.randrange(1,10)
guess = int(input("Enter any number  - "))
while n != guess:
    #if guess is small then n 
    if  guess < n :
        print(" too smaller from random no ")
        # take another input 
        guess = int(input("Try Again Enter any number  - "))
    elif guess > n : 
        print("your no is greater  then random number")      
        # again new value inpput
        guess = int(input("Enter new no again  - "))  
    else:
        break

print("you got the correct no '\U0001F602 \U0001F602 \U0001F602' ")     

