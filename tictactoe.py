    

def tic():
    gamee = [[1,1,1],[1,1,1],[1,1,1]]
    print(gamee[0])
    print(gamee[1])
    print(gamee[2])
    while(True):
#        while(gamee[r1][c1]!=1):
        r1 = int(input("Please enter the location in rows-player 1:"))

        while((r1>2) or (r1<0)) :
            print("Please enter a number between 0 and 2.")
            r1 = int(input("Please enter the location in rows-player 1:"))
#        if ((r1 > 2) or (r1 < 0)):
#            print("Please enter a number between 0 and 2.")
#            r1 = int(input("Please enter the location in rows-player 1:"))
        c1 = int(input("Please enter the location in columns-player 1:"))
#        if ((c1 > 2) or (c1 < 0)):
#            print("Please enter a number between 0 and 2.")
#            c1 = int(input("Please enter the location in columns-player 1:"))         think 
            
        while((c1>2) or (c1<0)) :
            print("Please enter a number between 0 and 2.")
            c1 = int(input("Please enter the location in columns-player 1:"))
#        if (gamee[r1][c1]!=1):
#            print("Please enter another number. The space is full.") 
            #run the while in the while again?

        while(gamee[r1][c1]!=1):
             print("Please enter another number. The space is full.")
             r1 = int(input("Please enter the location in rows-player 1:"))
             c1 = int(input("Please enter the location in columns-player 1:"))

        gamee[r1][c1] = "X"
        print(gamee[0])
        print(gamee[1])
        print(gamee[2])
        
        if (isOver(gamee) == False) :
            break#then while stop and tic stops use if

#FIX---
#        if ((r2 > 2) or (r2 < 0)):
#            print("Please enter a number between 0 and 2.")
#            r2 = int(input("Please enter the location in rows-player 2:"))
#        c2 = int(input("Please enter the location in columns-player 2:"))
#        if ((c2 > 2) or (c2 < 0)):
#            print("Please enter a number between 0 and 2.")
#            c2 = int(input("Please enter the location in columns-player 2:"))
#
#        while(gamee[r2][c2]!=1):
#            print("Please enter another number. The space is full.")
#            r2 = int(input("Please enter the location in rows-player 2:"))
#            if ((r2 > 2) or (r2 < 0)):
#                print("Please enter a number between 0 and 2.")
#                r2 = int(input("Please enter the location in rows-player 2:"))
#            c2 = int(input("Please enter the location in columns-player 2:"))
#            if ((c2 > 2) or (c2 < 0)):
#                print("Please enter a number between 0 and 2.")
#                c2 = int(input("Please enter the location in columns-player 2:"))

#        while(gamee[r2][c2]!=1):
        r2 = int(input("Please enter the location in rows-player 2:"))

        while((r2>2) or (r2<0)) :
            print("Please enter a number between 0 and 2.")
            r2 = int(input("Please enter the location in rows-player 2:"))
 #           if ((r2 > 2) or (r2 < 0)):
 #               print("Please enter a number between 0 and 2.")
#                r2 = int(input("Please enter the location in rows-player 2:"))
        c2 = int(input("Please enter the location in columns-player 2:"))
 #           if ((c2 > 2) or (c2 < 0)):
#                print("Please enter a number between 0 and 2.")
#                c2 = int(input("Please enter the location in columns-player 2:"))
#            if (gamee[r2][c2]!=1):
#               print("Please enter another number. The space is full.")
                #run the while again?
        while((c2<0) or (c2>2)) :
            print("Please enter a number between 0 and 2.")
            c2 = int(input("Please enter the location in columns-player 2:"))

        while(gamee[r2][c2]!=1):
             print("Please enter another number. The space is full.")
             r2 = int(input("Please enter the location in rows-player 2:"))
             c2 = int(input("Please enter the location in columns-player 2:"))
            

        gamee[r2][c2] = "O"
        print(gamee[0])
        print(gamee[1])
        print(gamee[2])

        result = getWinner(gamee)
        if (isOver(gamee) == False) :
            break
        
        


def getWinner(gamee):
    if ((gamee[0][0] == gamee[0][1]) and (gamee[0][2] == gamee[0][1]) and (gamee[0][2] == gamee[0][0])) :
        if gamee[0][0] == "O":
            return "player 2"
        if gamee[0][0] == "X":
            return "player 1"
    if ((gamee[1][0] == gamee[1][1]) and (gamee[1][2] == gamee[1][1]) and (gamee[1][2] == gamee[1][0])) :
        if gamee[1][0] == "O":
            return "player 2"
        if gamee[1][0] == "X":
            return "player 1"
    if ((gamee[2][0] == gamee[2][1]) and (gamee[2][2] == gamee[2][1]) and (gamee[2][2] == gamee[2][0])) :
        if gamee[2][0] == "O":
            return "player 2"
        if gamee[2][0] == "X":
            return "player 1"
    if ((gamee[0][0] == gamee[1][0]) and (gamee[2][0] == gamee[1][0]) and (gamee[0][0] == gamee[2][0])) :
        if gamee[0][0] == "O":
                return "player 2"
        if gamee[0][0] == "X":
                return "player 1"
    if ((gamee[0][1] == gamee[1][1]) and (gamee[2][1] == gamee[1][1]) and (gamee[2][1] == gamee[0][1])) :
        if gamee[0][1] == "O":
                return "player 2"
        if gamee[0][1] == "X":
                return "player 1"
    if ((gamee[0][2] == gamee[1][2]) and (gamee[2][2] == gamee[1][2]) and (gamee[2][2] == gamee[0][2])) :
        if gamee[0][2] == "O":
                return "player 2"
        if gamee[0][2] == "X":
                return "player 1"
    if ((gamee[0][0] == gamee[1][1]) and (gamee[2][2] == gamee[1][1]) and (gamee[2][2] == gamee[0][0])) :
        if gamee[0][0] == "O":
                return "player 2"
        if gamee[0][0] == "X":
                return "player 1"

    if ((gamee[0][2] == gamee[1][1]) and (gamee[2][0] == gamee[1][1]) and (gamee[2][0] == gamee[0][2])) :
        if gamee[0][2] == "O":
                return "player 2"
        if gamee[0][2] == "X":
                return "player 1"

def isOver(gamee):
    
    result = getWinner(gamee)
    
    #for i in range(0, 3):
    #    for a in range(0, 3):
    #        if (gamee[i][a]=="O" or gamee[i][a]=="X"):
    #            return False
    if ((result == "player 1") or (result == "player 2")) :
        print(result, "won")
        return False
    for i in range(0, 3):
        for a in range(0, 3):
            if (gamee[i][a]==1):
                return True
    print(result, "won")
    return False
    
#from practice import game
print(tic())