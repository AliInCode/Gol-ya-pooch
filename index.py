import random
playerName = str(input("Please Enter your Name : "))
choicePoint = int(input("please Enter your choice Point :"))
point = 0 

while True:
    print("1) right hand")
    print("2) left hand")
    Robot = random.randint(1,2)
    if Robot == 1:
        rightHand = "*"
        leftHand = ""
    elif Robot == 2 :
        rightHand = ""
        leftHand = "*"

    player_1 = int(input("Please Enter your choice : "))

    if player_1 == 1:
        rightHand_1 = "*"
        leftHand_1 = ""
    elif player_1 == 2 :
        rightHand_1 = ""
        leftHand_1 = "*"
    else :
        print("somthing wrong ....")

    if (rightHand ==  "*" and rightHand_1 == "*") or (leftHand == "*" and leftHand_1 == "*"):
        print("You guessed right")
        print("----------------------------------------------------------")
        point +=1
        print(f"right hand : {rightHand}")
        print(f"left hand : {leftHand}")
        print(f"{playerName}: {point}")
        print("----------------------------------------------------------")
    elif (rightHand ==  "" and rightHand_1 == "*") or (leftHand == "" and leftHand_1 == "*"):
        print("You guessed wrong")
        print("----------------------------------------------------------")
        point -=1
        print(f"right hand : {rightHand}")
        print(f"left hand : {leftHand}")
        print(f"{playerName}: {point}")
        print("----------------------------------------------------------")
    if point == choicePoint :
        print (f"{playerName} is winner....")
        point  = 0
        exit =  str(input("Do you Want continue? :")).lower()
        if exit =="y":
            print("--------------------------------------------------------")
            playerName = str(input("Please Enter your Name : "))
            choicePoint = int(input("please Enter your choice Point :"))
            print("--------------------------------------------------------")
            continue
        elif exit == "n":
            break
    elif point == -choicePoint:
        print (f"{playerName} is Loser....")
        point  = 0
        exit =  str(input("Do you Want continue? :")).lower()
        if exit =="y":
            print("--------------------------------------------------------")
            playerName = str(input("Please Enter your Name : "))
            choicePoint = int(input("please Enter your choice Point :"))
            print("--------------------------------------------------------")
            continue
        elif exit == "n":
            break
