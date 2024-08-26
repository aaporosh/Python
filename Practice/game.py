import random

print("*** Welcome to this Game ***")

while (True) :
    a = input("Do you want to continue this game Y or N ")

    if a=='Y' :
        ran = random.randint(1,3)
        n = int(input("What do you choose for 1.rock  2.paper  3.scissors "))

        if (n==ran) :
             print("Draw")

        elif n==1 and ran ==2 :
             print("\nYou choose Rock")
             print("Computer choose Paper\n")
             print("Computer win")

        elif n==2 and ran==3 :
            print("\nYou choose Paper")
            print("Computer choose Scissors\n")
            print("Computer win")

        elif n==1 and ran == 3 :
            print("\nYou choose Rock")
            print("Computer choose Scissors\n")
            print("You win")

        elif n==3 and ran ==1 :
            print("\nYou choose Scissors")
            print("Computer choose Rock\n")
            print("Computer win")

        elif n==2 and ran==1 :
            print("\nYou choose Paper")
            print("Computer choose Rock\n")
            print("You win")

        elif n ==3 and ran ==2  :
            print("\nYou choose Scissors")
            print("Computer choose Paper\n")
            print("You win")
        else :
            print("wrong input")
    else :
        print("Game Over")    