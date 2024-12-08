"""
DnD Battle Simulator
Dylan Rhymaun
Simulates a battle in Dungeons and Dragons
as a means of demonstrating the value
and function of the random module.
"""

import random

classes = ["barbarian", "rogue", "wizard"]
chosen_class = "none"
move1 = ""
move2 = ""
move3 = ""
player_hp = 30
goblin_hp = 50
goblin_max_hp = goblin_hp  
goblin_skips_turn = False  
goblin_accuracy = 1.0  

def whirlwind():
    """Barbarian's basic attack that deals 1d8 physical damage."""
    return random.randint(1, 8)

def phoenix():
    """Barbarian's attack that deals 1d8 fire damage."""
    return random.randint(1, 8)

def fight():
    """Barbarian's ability to heal 1d8 health."""
    return random.randint(1, 8)

def mortal(current_goblin_hp):
    """Rogue's ability to kill an enemy below 20% HP."""
    if current_goblin_hp < 0.2 * goblin_max_hp:  #Check against maximum HP
        return "Instant Kill"
    return 0  #No damage if not below the threshold

def sawtooth():
    """Rogue's attack that deals 1d4 physical and 1d4 bleed damage."""
    physical = random.randint(1, 4)
    bleed = random.randint(1, 4)
    return physical, bleed

def chloroform():
    """Rogue's ability to cause the enemy to lose a turn."""
    return random.choice([True, False])  #50%

def shocking():
    """Wizard's basic attack that deals 1d8 lightning damage."""
    return random.randint(1, 8)

def fear():
    """Wizard's ability to make the enemy lose a turn."""
    return random.choice([True, False])  #50%

def fog():
    """Wizard's spell to reduce enemy accuracy."""
    return "Enemy accuracy reduced for 2 turns"

############################################## Choosing a class ############################################################
if __name__ == '__main__':
    print("Welcome to Dylan's DnD battle simulator!")
    while chosen_class not in classes:
        chosen_class = input("What class would you like to play as? "
                             "Type 'Barbarian', 'Rogue', or 'Wizard': ").lower()
        if chosen_class not in classes:
            print("Invalid class. Please choose either 'Barbarian', 'Rogue', or 'Wizard'.")
    
    print(f"You have chosen the {chosen_class.capitalize()} class!")
    
    if chosen_class == "barbarian":
        print("You have access to (1) Whirlwind, (2) Phoenix Dive, and (3) Thick of the Fight")
        move1 = whirlwind
        move2 = phoenix
        move3 = fight
        
    elif chosen_class == "rogue":
        print("You have access to (1) Mortal Blow, (2) Sawtooth Knife, and (3) Chloroform")
        move1 = mortal
        move2 = sawtooth
        move3 = chloroform
        
    elif chosen_class == "wizard":
        print("You have access to (1) Shocking Grasp, (2) Cause Fear, and (3) Fog Cloud")
        move1 = shocking
        move2 = fear
        move3 = fog
        
############################################## Flavor/setup ############################################################
    print("You, a wayward adventurer come upon greenbog cave - fabled by townsfolk in the local "
          "village to be home to the forest's most fearsome band of goblins. ")
    if chosen_class == "barbarian":
        print("You draw your sword, light your torch, and slowly enter the mouth of the cave.")
    if chosen_class == "rogue":
        print("You draw your dagger, drink a potion of night vision, and creep into the abyss.")
    if chosen_class == "wizard":
        print("You draw your staff, cast magelight, and meander inside.")
    print("After a few minutes of turning corners and climbing over rubble, you begin "
          "to hear the sound of something ripping and gnawing through flesh and bones."
          "Passing through an opening into a larger cavern, you can make out the "
          "silhouette of a monster not 15 steps away. It's the band's leader!")
    if chosen_class == "barbarian":
        print("You empty your torch into a nearby brazier, engulfing the cavern in light. "
              "You ready your sword and charge forth.")
    if chosen_class == "rogue":
        print("You squint your eyes, ready your blade, and sneak up behind him.")
    if chosen_class == "wizard":
        print("You cast another magelight and prepare to fight.")
      
############################################### Battle Loop ###########################################################    
    while goblin_hp > 0 and player_hp > 0:
        print("\n")
        print("Choose your move:")
        if chosen_class == "barbarian":
            print("(1) Whirlwind")
            print("(2) Pheonix Dive")
            print("(3) Thick of the Fight")
        if chosen_class == "rogue":
            print("(1) Mortal Blade")
            print("(2) Sawtooth Knife")
            print("(3) Chloroform")
        if chosen_class == "wizard":
            print("(1) Shocking Grasp")
            print("(2) Cause Fear")
            print("(3) Fog Cloud")
        choice = input("Enter the number of your move: ")
       
        if choice == "1":
            if chosen_class == "rogue":  #Mortal Blow
                result = mortal(goblin_hp)
                if result == "Instant Kill":
                    goblin_hp = 0
                    print("You instantly killed the goblin!")
                else:
                    print("Mortal Blow failed. The goblin isn't weak enough!")
            else:
                damage = move1()
                print(f"You dealt {damage} damage!")
                goblin_hp -= damage
        
        elif choice == "2":
            if chosen_class == "rogue":  #Sawtooth Knife
                physical, bleed = sawtooth()
                print(f"You dealt {physical} physical damage and {bleed} bleed damage!")
                goblin_hp -= (physical + bleed)
            elif chosen_class == "wizard":  #Cause Fear
                if fear():
                    print("The goblin is terrified and loses its next turn!")
                    goblin_skips_turn = True
                else:
                    print("Your spell failed to cause fear.")
            else:  #Phoenix Dive
                damage = phoenix()
                print(f"You dealt {damage} fire damage!")
                goblin_hp -= damage
        
        elif choice == "3":
            if chosen_class == "barbarian":  #Thick of the Fight
                healing = fight()
                player_hp += healing
                print(f"You healed for {healing} HP! Your current HP is {player_hp}.")
            elif chosen_class == "wizard":  #Fog Cloud
                print("A thick fog surrounds the goblin, reducing its accuracy!")
                goblin_accuracy = 0.5
            elif chosen_class == "rogue":  #Chloroform
                if chloroform():
                    print("The goblin is knocked out and loses its next turn!")
                    goblin_skips_turn = True
                else:
                    print("Your attack failed to knock out the goblin.")
        
        else:
            print("Invalid choice. You lose your turn.")
        
        #Goblin's Turn
        if goblin_hp <= 0:
            print("The goblin has been defeated! You win!")
            break

        if goblin_skips_turn:
            print("The goblin is stunned and skips its turn!")
            goblin_skips_turn = False  # Reset
        else:  #Only execute the goblin's attack if it's not stunned
            print("\nThe goblin attacks!")
            if random.random() < goblin_accuracy:
                goblin_damage = random.randint(1, 6)
                player_hp -= goblin_damage
                print(f"The goblin dealt {goblin_damage} damage! \nYour HP: {player_hp}")
            else:
                print(f"The goblin misses! \nYour HP: {player_hp}")

        #Check player HP status
        if player_hp <= 0:
            print("You were defeated by the goblin! Too bad!")
            break

        #Display goblin's HP at the end of their turn
        print(f"Goblin's HP: {goblin_hp}")
