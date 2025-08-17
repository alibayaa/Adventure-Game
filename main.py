import random
import time
import sys


health = 100
damage = 25
monster_damage = 10

def menu():
    print("Escape The Maze")
    print("1. Start Game")
    print("2. Exit")

def start_game():
    y = 0
    while y < 10:
        print("You find yourself in a dark maze with no memory of how you got there.")
        movement = input("Left, Right, or Forward?: ")
        if movement.lower() == "left":
            print("You moved left.")
            random_event = random.randint(1, 10)
            if random_event % 2 != 0:
                battle()
                y += 1
            
            else:
                print("You advanced through the maze.")
                y += 1    
        elif movement.lower() == "right":
            print("You moved right.")
            random_event = random.randint(1, 11)
            if random_event % 2 != 0:
                battle()
                y += 1
            else:
                print("You advanced through the maze.")
                y += 1
        elif movement.lower() == "forward":
            print("You moved forward.")
            random_event = random.randint(1, 11)
            if random_event % 2 != 0:
                battle()
                y += 1
            else:
                print("You advanced through the maze.")      
                y += 1
        else:
            print("Invalid direction, please try again.")
            start_game()
    if y >= 10:
        print("Congratulations! You escaped the maze!")   

def battle():
    
    print("A monster appeared!")
    print("What do you want to do?")
    print("1. Fight")
    print("2. Run")
    action = input("Please select an action: ") 
    if action == "1":
        monster_health = 75
        while monster_health > 0:
            time.sleep(2)
            print("You attack the monster")
            time.sleep(3)
            monster_health -= damage
            print(f"You dealt {damage} damage to the monster. Monster health is now {monster_health}.")
            time.sleep(2)
            print("The monster attacks")
            time.sleep(3)
            global health 
            health -= monster_damage
            print(f"The monster dealt {monster_damage} damage. You have {health} remaining")
        if monster_health <= 0:
            print("The monster has been defeated!") 
            print (f"You won with {health} health remaining")
        elif health <= 0:
            print("You have been defeated.")
            print("Game Over")
            sys.exit()
    elif action == "2":
        flee = random.randint(1, 3)
        if flee == 2:
            print("You fled the battle and advanced through the maze.")
        else:
            print("You failed to flee the monster, prepare for battle!")
            monster_health = 75
            while monster_health > 0 and health > 0:
                time.sleep(2)
                print("You attack the monster")
                time.sleep(3)
                monster_health -= damage
                print(f"You dealt {damage} damage to the monster. Monster health is now {monster_health}.")
                time.sleep(2)
                print("The monster attacks")
                time.sleep(3)
                health -= monster_damage
                print(f"The monster dealt {monster_damage} damage. You have {health} remaining")
            if monster_health <= 0:
                print("The monster has been defeated!") 
                print (f"You won with {health} health remaining")
            elif health <= 0:
                print("You have been defeated.")
                print("Game Over")
                sys.exit()
    else:
        print("Invalid action, please try again.")
        battle()

def exit():
    print("Come back and play some time soon!")
    sys.exit()

def game():
      menu()
      x = input("Please select an option: ")
      if x == "1":
        start_game()
      elif x == "2":
        exit()
      else:
        print("Invalid option, please try again.")
        game()

game()