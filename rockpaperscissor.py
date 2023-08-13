def rps():
    import random
    roc = 1
    pap = 2
    sci = 3
    print("===Rock Paper Scissors Game===")
    YouSco = 0
    ComSco = 0
    for i in range(3):
        a = random.randint(1, 3)
        b = int(input("Choose one out of: 1. Rock 2. Paper 3. Scissors(only numbers)"))
        if (b>3 or b<1):
            print("please enter a number between 1 and 3")
        elif (b==a):
            print("tie.")
            print("==You:", YouSco, "Computer:", ComSco, "==")
        elif ((b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2)):
            YouSco = YouSco + 1
            print("You Win!")
            print("==You:", YouSco, "Computer:", ComSco, "==")
        elif ((a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2)):
            ComSco = ComSco + 1
            print("You lost...")
            print("==You:", YouSco, "Computer:", ComSco, "==")
    if (YouSco>ComSco): 
            print("------------------------")
            print("FINAL SCORE: ==You:", YouSco, "Computer:", ComSco, "==")
            print("YOU ARE THE WINNER!")
    elif (YouSco==ComSco): 
            print("------------------------")
            print("FINAL SCORE: ==You:", YouSco, "Computer:", ComSco, "==")
            print("YOU ARE TIED WITH THE COMPUTER")
    elif (YouSco<ComSco): 
            print("------------------------")
            print("FINAL SCORE: ==You:", YouSco, "Computer:", ComSco, "==")
            print("YOU LOST")

def rps_playagain():
    c = ""
    while(c!="y" and c!="n"): 
            c = str(input("Do you want to play this game again?(y/n)"))
            if (c=="y"):
                return True
            elif (c=="n"):
                return False
                break
            print("please enter either y or n")
            
rps()
while(rps_playagain()):
    rps()

