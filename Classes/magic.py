import random
from colorama import init, Fore, Back, Style

init()

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg  = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def enemies_attack_or_heal(self, user, target):

        if self.get_type() == "white":
            dmg = self.generate_damage()
            user.heal(dmg)
            print(user.name + " casts " + self.name + "!")
            print(user.name + " healed for " + Fore.LIGHTBLUE_EX + str(dmg) + Style.RESET_ALL + "!" )
        
        else:
            dmg = self.generate_damage()
            target.take_damage(dmg)
            print(user.name + " casts " + self.name + "!")
            print(Fore.RED + target.name + " took ", str(dmg) + " points of damage." + Style.RESET_ALL)
            user.reduce_mp(self.get_cost())

        