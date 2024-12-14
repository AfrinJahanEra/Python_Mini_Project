def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You're in a dark forest. Choose your path:")
    
    choice1 = input("Do you go left or right? ").lower()
    if choice1 == "left":
        print("You encounter a river.")
        choice2 = input("Do you swim across or walk along the river? (swim/walk): ").lower()
        if choice2 == "swim":
            print("You were eaten by a crocodile. Game over!")
        else:
            print("You found a bridge and crossed safely. You win!")
    elif choice1 == "right":
        print("You encounter a cave.")
        choice2 = input("Do you enter the cave or go back? (enter/back): ").lower()
        if choice2 == "enter":
            print("You found hidden treasure! You win!")
        else:
            print("You got lost in the forest. Game over!")
    else:
        print("Invalid choice. Game over!")

adventure_game()
