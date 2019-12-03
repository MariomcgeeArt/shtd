import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        random_value = random.randint(0,self.max_damage)
        return random_value

    
    
    
    
    
    
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0,self.max_block)
        return random_value


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):

        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        
    
        





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # # If you run this file from the terminal
    # # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())
    my_hero = Hero("Grace Hopper",2000)
    print(my_hero.name)
    print(my_hero.current_health)