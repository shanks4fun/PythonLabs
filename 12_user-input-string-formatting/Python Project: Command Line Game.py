def start_game():
    print("Welcome to dungeons and dragons!")
    player_name = input("What is thy name adventurer? ")
    print(f"\nHello, {player_name}! Good luck to you!")

    main_room(player_name, has_sword=False)

def main_room(player_name, has_sword):
    print("You find yourself in a dark room with two doors.")
    print("One door is to your left and the other is to your right.")
    
    while True:
        choice = input("Which door do you choose? (left/right): ").lower()
        
        if choice == 'left':
            has_sword = empty_room(has_sword)
        elif choice == 'right':
            dragon_room(player_name, has_sword)
            break
        else:
            print("Please choose 'left' or 'right'.")

def empty_room(has_sword):
    print("\nYou enter an empty room. It seems to be just a plain old room.")
    print("You can choose to look around or return to the previous room.")
    
    while True:
        choice = input("What do you want to do? (look/return): ").lower()
        
        if choice == 'look':
            print("You look around and find a sword lying on the ground.")
            take_sword = input("Do you want to take the sword? (yes/no): ").lower()
            if take_sword == 'yes':
                print("You have taken the sword and return to the previous room.")
                has_sword = True
                break
            elif take_sword == 'no':
                print("You leave the sword and return to the previous room.")
                break
            else:
                print("Please choose 'yes' or 'no'.")
        elif choice == 'return':
            print("You return to the previous room.")
            break
        else:
            print("Please choose 'look' or 'return'.")
    
    return has_sword  # Return the updated sword status

def dragon_room(player_name, has_sword):
    print("\nYou enter the room and encounter a fearsome dragon!")
    print("The dragon looks at you with hungry eyes.")
    
    while True:
        choice = input("Do you want to fight the dragon? (yes/no): ").lower()
        
        if choice == 'yes':
            if has_sword:
                print("You use the sword to defeat the dragon. Congratulations, you win!")
                break
            else:
                print("Without a sword, you are no match for the dragon. You are eaten and lose the game.")
                break
        elif choice == 'no':
            print("You decide not to fight the dragon and return to the previous room.")
            main_room(player_name, has_sword)  # Return to the main game loop with the current state
            break
        else:
            print("Please choose 'yes' or 'no'.")

# Start the game
start_game()
