import random
from colorama import Fore, Style, Back, init

init()
class Person:
    def __init__(self, name, hp, atk, mp, df, mgc, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.mgc = mgc
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    

    def take_damage(self, dmg):
        self.hp -= dmg
 
        if self.hp<0:
            self.hp = 0

        return self.hp


    def get_hp(self):
        return self.hp


    def get_max_hp(self):
        return self.maxhp


    def get_max_mp(self):
        return self.maxmp
    

    def get_mp(self):
        return self.mp


    def reduce_mp(self, cost):
        self.mp -= cost
    

    def choose_action(self):
        i = 1
        print("\n" + Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + "Actions:" + Style.RESET_ALL)
        print("\n" + Style.BRIGHT + self.name + Style.RESET_ALL)
        for item in self.actions:
            print("     " + str(i) + ":", item)
            i += 1


    def choose_magic(self):
        i = 1
        print("\n" + Fore.BLUE + Style.BRIGHT + "Magic:" + Style.RESET_ALL)
        for spell in self.mgc:
            print("     " + str(i) + ":", spell.get_name(), "(Cost:"+ str(spell.get_cost()) +"mp)")
            i += 1


    def choose_target(self, targets):
        i=0
        print("\n" + Fore.RED + Style.BRIGHT + "TARGETS:" + Style.RESET_ALL)
        while i < len(targets):
            if targets[i].hp != 0:
                print("     " + str(i + 1) + ": " + targets[i].name)
            i += 1

        while True:
            try:
                target_choice = int(input("Choose target: ")) - 1
            except:
                print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                continue

            if target_choice < 0 or target_choice >= len(targets):
                print(Style.BRIGHT + Fore.RED + "Invalid input!" + Style.RESET_ALL)
                continue
            else:
                return targets[target_choice]


    def choose_item(self):
        i=1

        print("\n" + Fore.GREEN + Style.BRIGHT  + "Items:" + Style.RESET_ALL)
        for item in self.items:
            print("     " + str(i) + ":", item["item"].name, "(" + item["item"].description + ") (x" + str(item["quantity"]) +")")
            i += 1
        
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def enemy_stats(self):
        hp_bars = int(self.hp*50/self.maxhp)*"█"
        hp_spaces = (50-int(self.hp*50/self.maxhp))*" "
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        hp_string_spaces = ""

        if len(hp_string) < 9:
            dif = 9 - len(hp_string)
            hp_string_spaces += dif*" "

        print("\n" + Style.BRIGHT + self.name, hp_string_spaces + hp_string + "   |" + Fore.RED + hp_bars + hp_spaces 
        + Fore.WHITE + "|" + Style.RESET_ALL)



    def get_stats(self):
        #Doing a rule of three, the program determines how many bars are needed
        hp_bars = int(self.hp*25/self.maxhp)*"█"
        hp_spaces = (25-int(self.hp*25/self.maxhp))*" "
        mp_bars = int(self.mp*10/self.maxmp)*"█"
        mp_spaces = (10-int(self.mp*10/self.maxmp))*" "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        hp_string_spaces = ""
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        mp_string_spaces = ""

        if len(hp_string) < 9:
            dif = 9 - len(hp_string)
            hp_string_spaces += dif*" "
        
        if len(mp_string_spaces) < 9:
             dif = 9 - len(mp_string)
             mp_string_spaces += dif*" "

        print(Style.BRIGHT + self.name, hp_string_spaces + hp_string + "   |" + Fore.GREEN + hp_bars + hp_spaces 
        + Fore.WHITE + "|   " + mp_string_spaces + mp_string + "   |" + Fore.BLUE + mp_bars + mp_spaces 
        + Style.RESET_ALL + "|")

    def choose_enemy_spell(self):

        enemy_choice = random.randrange(0, len(self.mgc))
        spell = self.mgc[enemy_choice]
        
        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            return self.choose_enemy_spell()
        else:
            return spell
    



