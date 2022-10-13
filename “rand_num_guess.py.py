#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 6, 2022
# This program checks if the number is 7 
import random 

def main():
    #The random number generator 
    rand_num = random.randint(0,9)

    #Get numbers that you can guess
    ran_num = int(input("Enter a number between 0 and 9: "))
    print()
   
    if ran_num == rand_num:
        print("You guessed correct")    
    if ran_num != rand_num:
        print("You guessed wrong < The correct answer is {}>".format(rand_num))

if __name__ == "__main__":
    main()