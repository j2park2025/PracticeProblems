def game():
    import random
    b = random.randint(0, 100)
    i = 0
    print("Guessing Numbers game")
    print("=====================")
    for i in range(11):
        a = int(input("-------------------enter number:"))
        if (i==10):
            print("You used up all of your guesses! The real number was", b)
        elif (a==b):
            print("Correct! You got the answer in just", i+1, "trials!")

        elif (a>b):
            print("Incorrect...you used", i+1, "trials. The number is smaller than this!")
        elif (a<b):
            print("Incorrect...you used", i+1, "trials. The number is bigger than this!")
        

def game_continue():
        #c = str(input("Do you want to play this game again?"))
        c = ""
        while(c!="y" and c!="n"):  
            c = str(input("Do you want to play this game again?(y/n)"))
            if (c=="y"):
                return True
            elif (c=="n"):
                return False
                break
            print("please enter either y or n")
            
        

 # if((c!="y") and (c!="n")):
#
game()
while(game_continue()):
    game()
