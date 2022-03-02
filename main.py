from Classes.game import Person
from Classes.magic import Spell
from Classes.inventory import Item
from colorama import init, Fore, Back, Style
import random


init() #Start colorama

''''
print("\n\n")
print("NAME              HP                            MP        ")#10 spaces
print("                  _________________________             __________")
print(Style.BRIGHT + "Valos: 460/460   |" + Fore.GREEN + "█████████████████████████" + Fore.WHITE + "|   65/65   |"
         + Fore.BLUE +"██████████" + Style.RESET_ALL + "|")
'''


#Black Magic Instantiation
fire    = Spell(Fore.LIGHTRED_EX + "Fire" + Style.RESET_ALL, 10, 300, "black")
thunder = Spell(Fore.LIGHTYELLOW_EX + "Thunder" + Style.RESET_ALL, 10, 300, "black")
blizzard = Spell(Fore.LIGHTCYAN_EX + "Blizzard" + Style.RESET_ALL, 10, 300, "black")
meteo = Spell(Fore.LIGHTMAGENTA_EX + "Meteo" + Style.RESET_ALL, 30, 1000, "black")
quake = Spell(Fore.LIGHTMAGENTA_EX + "Earthquake" + Style.RESET_ALL, 14, 650, "black")


#White Magic Instantiation
cure = Spell(Fore.LIGHTBLUE_EX + "Cure" + Style.RESET_ALL, 12, 620, "white")
cura = Spell(Fore.LIGHTBLUE_EX + "Cura" + Style.RESET_ALL, 18, 2200, "white")


#Create items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item ("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item ("Super Potion", "potion", "Heals 500HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores MP/HP of one member of the party", 9999)
hielixer = Item ("MegaElixer", "elixer", "Fully restores part's MP/HP", 9999)
bomb = Item("Bomb", "attack", "Deals 500 points of damage by exploding", 500)

#Declare spells and items
player_spells = [fire, thunder, blizzard, meteo, quake, cure, cura]
player_items = [{"item":potion, "quantity": 5}, {"item":hipotion, "quantity": 5},
                {"item":superpotion, "quantity": 5}, {"item":elixer, "quantity": 5},
                {"item":hielixer, "quantity": 2}, {"item":bomb, "quantity": 5}]

enemy_spells = [fire, quake, cura]
magus_spells = [meteo,thunder, cure, cura]

#Instantiate People
player1 = Person("Diego ", 1560, 85, 120, 54, player_spells, player_items) #3560
player2 = Person("Andrés", 1560, 60, 200, 34, player_spells, player_items) #4460
player3 = Person("Jammu ", 1700, 72, 160, 40, player_spells, player_items) #3700

enemy2 = Person("Mage1 ", 1250, 100, 999, 325, enemy_spells, []) #1250
enemy1 = Person("Magus", 11200, 1200, 999, 70, magus_spells, []) #11200
enemy3 = Person("Mage2 ", 1250, 100, 999, 325, enemy_spells, []) #1250

players = [player1, player2, player3]
enemies = [enemy2, enemy1, enemy3]

defeated_enemies = 0
defeated_players = 0

turn = 1
running = True

print(Style.BRIGHT + Fore.RED + "AN ENEMY ATTACKS!" + Style.RESET_ALL)
choice = 0

enemy = enemies[0]

while running:
        if running == False:
                break

        print("==============================") #30 equal signs
        print(Style.BRIGHT + Fore.CYAN + "TURN #" + str(turn) + Style.RESET_ALL)
        print("\n\n")
        print(Style.BRIGHT + Fore.GREEN + "========YOUR PARTY'S TURN!========" + Style.RESET_ALL)
        for player in players:
                for enemyx in enemies:
                        enemyx.enemy_stats()

                print("\n")

                for playerx in players:
                        print("NAME               HP                                      MP        ")#10 spaces
                        playerx.get_stats()

                player.choose_action()

                try:
                        choice = int(input("Choose action: ")) - 1
                except:
                        print("Invalid Input! Letters or symbols are not allowed!")
                        continue

                if choice == 0:
                        dmg = player.generate_damage()
                        enemy = player.choose_target(enemies)
                        enemy.take_damage(dmg)
                        print(enemy.name + " took", str(dmg) + " points of damage.")
                
                elif choice == 1:
                        invalid = True
                        while invalid:
                                player.choose_magic()

                                try:
                                        choice = int(input("Choose a spell: ")) - 1
                                except:
                                        print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                                        continue

                                if choice < 0 or choice >= len(player.mgc):
                                        if choice == -1:
                                                break

                                        print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                                        continue
                                else:
                                        spell = player.mgc[choice].get_name()
                                        mpcost = player.mgc[choice].get_cost()
                                        current_mp = player.get_mp()

                                        if mpcost > current_mp:
                                                print(Style.BRIGHT + Fore.RED + player.name + " doesn't have enough mp! Choose another one!" + Style.RESET_ALL)
                                                print("If you have MP = 0 then write 0 !")
                                                continue
                                        
                                        else:
                                                invalid = False
                        
                        if choice == -1:
                                continue

                        if player.mgc[choice].get_type() == "white":
                                dmg = player.mgc[choice].generate_damage()
                                player.heal(dmg)
                                print(player.name + " casts " + spell + "!")
                                print("You healed for" + Fore.LIGHTBLUE_EX, dmg, "!" + Style.RESET_ALL)


                        else:
                                dmg = player.mgc[choice].generate_damage()
                                enemy = player.choose_target(enemies)
                                enemy.take_damage(dmg)
                                print(player.name + " casts " + spell + "!")
                                print(enemy.name + " took", str(dmg) + " points of damage.")
                                player.reduce_mp(player.mgc[choice].get_cost())
                
                elif choice == 2:
                        player.choose_item()
                        invalid = True
                        while invalid:
                                try:
                                        choice = int(input("Choose an item: ")) - 1
                                except:
                                        print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                                        continue
                                
                                if choice < 0 or choice >= len(player.items):
                                        if choice == -1:
                                                break
                                        print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                                        print("If you don't have any item or you don't want to use any, write 0!")
                                        continue
                                else:
                                        invalid = False
        
                        if choice == -1:
                                continue

                        item = player.items[choice]["item"]
                        player.items[choice]["quantity"] -= 1
                        item_quantity = player.items[choice]["quantity"]
                        ''''
                        if item_quantity < 0:
                                player.items[choice]["quantity"] = 0
                                print(Fore.RED + "You don't have any "+ item.name + "s!" + Style.RESET_ALL)
                                choice = -1
                                continue
                        '''                            

                        if item.type == "potion":
                                print("You used a " + item.name + "!")
                                player.heal(item.prop)
                                print("It heals for", item.prop, "HP points!")
                                
                        elif item.type == "elixer":
                                print("You used a " + item.name + "!")
                                if item.name == "MegaElixer":
                                        for player_to_heal in players:
                                                player_to_heal.hp = player_to_heal.get_max_hp()
                                                player_to_heal.mp = player_to_heal.get_max_mp()

                                if item.name == "Elixer":
                                        player.hp = player.get_max_hp()
                                        player.mp = player.get_max_mp()
                                                
                                print(Fore.GREEN + item.name + " fully restores HP and MP!" + Style.RESET_ALL)


                        elif item.type == "attack":
                                enemy = player.choose_target(enemies)
                                enemy.take_damage(item.prop)
                                print("You used a " + item.name + "!")
                                print(Fore.RED + "*BOOOOOOOOM*" + Style.RESET_ALL)
                                print(Fore.RED + "The " + item.name + " deals " + str(item.prop) + " points of damage to " + enemy.name 
                                + "!" + Style.RESET_ALL)
                        
                        i = 0
                        for item in player.items:
                                if item["quantity"] == 0:
                                        del player.items[i]
                                i += 1
                                
                                


                else:
                        print("You did not know what to do!")
                
                #Each time a player does something, the program checks how many defeated enemies there are
                i = 0
                for enemyx in enemies:
                        if enemyx.get_hp() == 0:
                                print(Style.BRIGHT + Fore.RED + enemyx.name + " was defeated!" + Style.RESET_ALL)
                                del enemies[i]
                                i -= 1
                                defeated_enemies += 1
                        
                        i += 1
                #If there are three defeated enemies, the player wins
                if defeated_enemies == 3:
                                print(Fore.GREEN + "You have defeated everyone! \nYou Won! Congratulations!" + Style.RESET_ALL)
                                running = False
                                break
        
        if running == False:
                break
        
        #If there are still enemies, it's their turn
        print(Style.BRIGHT + Fore.RED + "======== ENEMY'S TURN! ======== \n" + Style.RESET_ALL)
        for enemy in enemies:
                enemy_choice = random.randrange(0, 2)

                if enemy.name == "Magus" and enemy.mp >= 10:
                        enemy_choice = 1

                target = random.randrange(0, len(players))

                if enemy_choice == 1:

                        spell = enemy.choose_enemy_spell()
                        spell.enemies_attack_or_heal(enemy, players[target])

                elif enemy_choice == 0:
                        enemy_damage = enemy.generate_damage()
                        players[target].take_damage(enemy_damage)                                
                        print(enemy.name +" attacks! " + Fore.RED + players[target].name +" took", str(enemy_damage) + " points of damage!" + Style.RESET_ALL)


        #After the enemies attack, the code checks how many defeated players there are
        i = 0
        for playerz in players:
                if playerz.get_hp() == 0:
                        print(Style.BRIGHT + Fore.RED + playerz.name +" was defeated!" + Style.RESET_ALL)
                        del players[i]
                        i -= 1
                        defeated_players += 1
                i += 1 
        #If there are 3 defeated players, the player lose.
        if defeated_players == 3:
                        print(Fore.RED + " Oh no! Your whole party was defeated! Your enemies won!")
                        running = False
                        break
        turn += 1

input("Input something to end the program: ")
