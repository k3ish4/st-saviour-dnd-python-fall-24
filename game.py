import time
import random
from tav import Tav

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print('Genshin Impact')


    print_dramatic_text("You awake after seemingly washing up on the shore of a strange land. A small floating creature with white hair and a pecuilar outfit hovers worriedly over your seemingly lifeless body until you finally become responsive.")
    print_dramatic_text("The creature introduces herself to you as Paimon, and then asks about your own identity.")
    name = input("What is your name, traveller? ")
    weapons = ['claymore', 'bow', 'sword', 'polearm', 'catalyst']
    print(weapons)
    weapon = input("What weapon do you wield? ")
    while weapon.lower() not in weapons:
        weapon = input("That weapon does not yet exist in this world. What weapon do you weild? ")

    
    player = Tav(name, weapon)
    view_stats = input(("If you wish to see your current stats, type 'stats'. "))
    if view_stats.lower() == 'stats':
        print("")
        player.print_character_sheet()
        print("")
 

    print_dramatic_text("As you and Paimon wander around this strange land, she tells you that you are currently in the nation of Mondstadt, the land of freedom.")
    print_dramatic_text("Your conversation is interrupted by a small slime. It jumps out at you and does some damage despite its seemingly harmless appearance.")

    print_dramatic_text("")
    print_dramatic_text("-------BATTLE--------")
    
    slime_maxhp = 20
    slime_hp = slime_maxhp
    
    moves = ['normal attack', 'skill', 'shield', 'burst']

    print_dramatic_text("Your first battle has begun! You can choose to fight monsters with four different types of moves: 'normal attack,' 'skill,' 'shield,' and 'burst'.")
    print_dramatic_text("In order to attack the slime with a normal attack, type 'normal attack'. The damage done by your normal attack, skill, and burst will scale off of your ATK stat.  ")
    print_dramatic_text("In order to attack the slime with your special skill, type 'skill'. This attack does more damage than a normal attack, but it cannot be used back to back.")
    print_dramatic_text("In order to defend yourself against the monster's next blow, type 'shield'. This move absorbs a portion of the damage that the monster deals. ")
    print_dramatic_text("In order to attack the slime with your burst, type 'burst'. This attack does even more damage than your skill, But it can only be used once your energy is maxxed out. Your energy will increase by 5 with each normal attack, skill, or shield you use.")
    print_dramatic_text("")
    print_dramatic_text("Good luck on your first battle! You may now take the first swing")
    
    used_skill = False
    while slime_hp > 0:
        player_attack = input()
        
        if player_attack.lower() == "normal attack":
            damage_dealt = int(random.uniform(player.ATK * .1, player.ATK * 0.2))
            slime_hp -= damage_dealt
            if (damage_dealt) == (player.ATK * 0.3):
                print("CRITICAL HIT!")
            print("You struck the monster with your " + player.weapon + ". Slime has taken " + str(damage_dealt) + " damage. " + str(slime_hp) + " hp remaining.")
            if slime_hp > 0:
                slime_damage = int(random.uniform(player.MAXHP * .1, player.MAXHP * .15))
                player.CurrentHP -= slime_damage
                print("Slime lunges at you and deals " + str(slime_damage) + " damage. You have " + str(player.CurrentHP) + " hp remaining.")
                print("")
            player.Energy += 5
            used_skill = False

        if player_attack.lower() == "skill":
            if used_skill:
                print('You have already used a skill in this encounter!')
                print('')
            else:
                damage_dealt = int(random.uniform(player.ATK * .2, player.ATK * 0.3))
                slime_hp -= damage_dealt
                if (damage_dealt) >= (player.ATK * 0.35):
                    print("CRITICAL HIT!")
                    print("")
                print("You struck the monster with your " + player.weapon + ". Slime has taken " + str(damage_dealt) + " damage. " + str(slime_hp) + " hp remaining.")
                if slime_hp > 0: 
                    slime_damage = int(random.uniform(player.MAXHP * .1, player.MAXHP * .2))
                    player.CurrentHP -= slime_damage
                    print("Slime lunges at you and deals " + str(slime_damage) + " damage. You have " + str(player.CurrentHP) + " hp remaining.")
                    print("")
                player.Energy += 5
                used_skill = True
            
        if player_attack.lower() == "shield":
            slime_damage = int(((random.uniform(player.MAXHP * .1, player.MAXHP * .2)) - (player.DEF * 0.1)))
            player.CurrentHP -= slime_damage
            print("Slime lunges at you and deals " + str(slime_damage) + " damage. You have " + str(player.CurrentHP) + " hp remaining.")
            print("")
            player.Energy += 5
            used_skill = False

        if player_attack.lower() == "burst": 
         if player.Energy < player.MAXEnergy:
             print("You don't have enough energy to use your burst yet! You need " + str(player.MAXEnergy - player.Energy) + " more energy. Try using another attack. \n ")
         else:
                damage_dealt = int(random.uniform(player.ATK * .4, player.ATK * .5))
                slime_hp -= damage_dealt
                if (damage_dealt) >= player.ATK:
                    print("CRITICAL HIT!")
                    print("")
                print("A great power surges through you as you deal a heavy blow to the monster with your " + player.weapon + ". Slime has taken " + str(damage_dealt) + " damage. " + str(slime_hp) + " hp remaining.")
                if slime_hp > 0:
                    slime_damage = int(random.uniform(player.MAXHP * .1, player.MAXHP * .15))
                    player.CurrentHP -= slime_damage
                    print("Slime lunges at you and deals " + str(slime_damage) + " damage. You have " + str(player.CurrentHP) + " hp remaining.")
                    print("")
                player.Energy == 0   
                used_skill = False
        
        if player_attack.lower() not in moves:
            print("That fighting style does not yet exist in this world. Try something else. \n ")

        while player.CurrentHP <= 0:
            slime_hp == slime_maxhp
            revival = input(print("Beware of enemies!\nWhenever you're ready, type 'revive' to heal yourself and redo this battle."))
            if revival.lower() != "revive":
                print("Whenever you're ready, type 'revive' to heal yourself and redo this battle.")
            else:
                print("Rethink your strategy and take on this monster once more!")
                player.CurrentHP = player.MAXHP

    player.level += 1
    player.ATK += (0.5 * player.ATK)
    player.DEF += (0.5 * player.DEF)
    player.MAXHP += (0.5 * player.MAXHP)
    player.CurrentHP = player.MAXEnergy
    player.MAXEnergy -=  5

    print("")
    print_dramatic_text("Congratulations " + player.name + "!. You have defeated your first monster!")
    print("")

