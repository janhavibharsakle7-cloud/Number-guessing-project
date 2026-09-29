# let us make a number guessing game  

import random 

# first for getting a random number 

# Generate a random number between 1 and 1000

Random_secretNo = random.randint(1, 1000)
guess = 0

# ask if the person is ready or not 
  
Ask_ = str(input("ARE YOU READY:"))


# lets start the game 

print(">>>>>>>>>>>>>LET'S START THE GAME<<<<<<<<<<<<<<")

print("I have thought of a random number between 1 to 1000")

# this loop is going to work until the guess is correct  

while guess !=Random_secretNo:

    guess = int(input("make a guess of a number of your choice:"))
    
    if guess < Random_secretNo:
        print("###### LOW #######")
        print("the number you guessed is low.")
        print ("guess a bigger number. ")


    elif guess > Random_secretNo:
         print("########## HIGH ############")
         print("the number you guessed is high.")
         print ("guess a smaller  number .")
    else:
        print("----------CONGRATULATIONS------------")
        print("*************YOU WON********************")
        print("the number you guessed is correct ")

print("!!!!!!!!!!! GAME IS COMPLETED !!!!!!!!!!!!!")
print("~~~~~~~~~~~~~~ PLAY AGAIN ~~~~~~~~~~~~~~~~`")
