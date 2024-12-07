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
        # Player's turn
        print("\nIt's your turn!")
        print("Choose your move:")
        print(f"(1) {move1.__name__.replace('_', ' ').capitalize()}")
        print(f"(2) {move2.__name__.replace('_', ' ').capitalize()}")
        print(f"(3) {move3.__name__.replace('_', ' ').capitalize()}")
            
        choice = input("Enter the number of your move: ")
        
        if choice == "1":
            damage = move1()
            if isinstance(damage, tuple):  # Handle multi-effect moves (e.g., sawtooth knife)
                print(f"You dealt {damage[0]} physical damage and {damage[1]} bleed damage!")
                goblin_hp -= (damage[0] + damage[1])
            else:
                print(f"You dealt {damage} damage!")
                goblin_hp -= damage
        
        elif choice == "2":
            damage_or_effect = move2(goblin_hp) if chosen_class == "rogue" else move2()
            if damage_or_effect == "Instant Kill":
                print("You executed a mortal blow! The goblin is defeated!")
                goblin_hp = 0
            elif isinstance(damage_or_effect, int):
                print(f"You dealt {damage_or_effect} damage!")
                goblin_hp -= damage_or_effect
            else:
                print("Your move caused an effect on the goblin!")
        
        elif choice == "3":
            if chosen_class == "barbarian":
                healing = move3()
                player_hp += healing
                print(f"You healed for {healing} HP! Your current HP is {player_hp}.")
            else:
                print("Your move caused an effect on the goblin!")
        
        else:
            print("Invalid choice. You lose your turn.")
        
        # Check if goblin is defeated
        if goblin_hp <= 0:
            print("The goblin has been defeated! You win!")
            break
