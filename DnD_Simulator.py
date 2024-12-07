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

def whirlwind():
    """Barbarian's basic attack that deals 1d8 physical damage."""
    return random.randint(1, 8)

def phoenix():
    """Barbarian's attack that deals 1d8 fire damage."""
    return random.randint(1, 8)

def fight():
    """Barbarian's ability to heal 1d8 health."""
    return random.randint(1, 8)

def mortal(enemy_hp):
    """Rogue's ability to kill an enemy below 20% HP."""
    if enemy_hp < 0.2 * enemy_hp:  
        return "Instant Kill"
    return 0  # No damage if not below threshold

def sawtooth():
    """Rogue's attack that deals 1d4 physical and 1d4 bleed damage for 2 turns."""
    physical = random.randint(1, 4)
    bleed = random.randint(1, 4)
    return physical, bleed

def chloroform():
    """Rogue's ability to cause the enemy to lose a turn."""
    success = random.choice([True, False])  # 50% chance of success
    return success

def shocking():
    """Wizard's basic attack that deals 1d8 lightning damage."""
    return random.randint(1, 8)

def fear():
    """Wizard's ability to make the enemy lose a turn."""
    success = random.choice([True, False])  # 50% chance of success
    return success

def fog():
    """Wizard's spell to reduce enemy accuracy for 2 turns."""
    return "Enemy accuracy reduced for 2 turns"

##########################################################################################################
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
        move1 = whirlwind #basic attack that does 1d8 physical dmg
        move2 = phoenix #basic attack that does 1d8 fire dmg
        move3 = fight #heals self 1d8
        
    if chosen_class == "rogue":
        print("You have access to (1) Mortal Blow, (2) Sawtooth Knife, and (3) Chloroform")
        move1 = mortal #kills enemies below 20% HP
        move2 = sawtooth #basic attack that does 1d4 physical and 1d4 bleed for 2 turns
        move3 = chloroform #if successful, enemy loses a turn
        
    if chosen_class == "wizard":
        print("You have access to (1) Shocking Grasp, (2) Cause Fear, and (3) Fog Cloud")
        move1 = shocking #basic attack that does 1d8 lightning dmg
        move2 = fear #if successfulm causes enemy to lose a turn
        move3 = fog #reduces enemy accuracy for 2 turns
        
##########################################################################################################
    print("You, a wayward adventurer come upon greenbog cave - fabled by townsfolk in the local "
          "village to be home to the forest's most fearsome band of goblins. ")
    if chosen_class == "barbarian":
        print("You draw your sword, light your torch, and slowly enter the mouth of the cave.")
    if chosen_class == "rogue":
        print("You draw your dagger, drink a potion of night vision, and creep into the cavern.")
    if chosen_class == "wizard":
        print("You draw your staff, cast magelight, and meander inside.")
    
    
