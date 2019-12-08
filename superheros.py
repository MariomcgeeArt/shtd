import random



class Ability:  
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)
        # may need to turn these into strings 



class Weapon (Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)



class Armor:
    def __init__(self, name, max_block):
        self.name = name 
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)



class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0
        self.abilities= []
        self.armors= []

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)     

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total
            
    def defend(self, damage_amt=0):
        blocked = 0
        for armor in self.armors:
            blocked += armor.block()
        return abs(blocked - damage_amt)

    def take_damage(self, damage=0):
        hit = self.defend(damage)
        self.current_health = self.current_health - hit

    def add_kill(self,num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def is_alive(self):
        alive = True
        if self.current_health > 0:
            return alive  
        elif self.current_health <= 0:
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            if not self.abilities and not opponent.abilities:
                print("DRAW! ")
                return

            # v1 = self.attack()
            # v2 = opponent.attack()
            opponent.take_damage(self.attack())
            
            self.take_damage(opponent.attack())
            
            if opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_deaths(1)
                print(f" {self.name} Wins! ")
                print(f"{opponent.name} is DEAD! ")
                return

            elif self.is_alive() == False:
                opponent.add_kill(1)
                self.add_deaths(1)
                print(f" {opponent.name} Wins! ")
                print(f"{self.name} is DEAD! ")
                return



class Team:
    def __init__(self,name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def view_all_heroes(self):
        for index, list_item in enumerate(self.heroes):
            print("{} {}".format(index, list_item.name))

    def add_hero(self, hero):
        self.heroes.append(hero)

    def get_alive(self):
        alive = []
        for heroes in self.heroes:
            if heroes.is_alive():
                alive.append(heroes)
        return alive

    def attack(self, other_team):

        while len(self.get_alive()) > 0 and len(other_team.get_alive()) > 0:
            H1 = random.choice(self.get_alive())
            H2 = random.choice(other_team.get_alive())
            H1.fight(H2)
                   
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} has K/D of {hero.kills} {hero.deaths} ! ")
            


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Give your Hero an Ability!: ")
        power = int(input('Give the Ability a power level: '))
        ability = Ability(name,power)
        return ability

    def create_weapon(self):
        name = input("Give your Hero a Weapon!: ")
        power = int(input('Give the Weapon a power level: '))
        weapon = Weapon(name,power)
        return weapon

    def create_armor(self):
        name = input("Give your Hero some Armor!: ")
        defense = int(input('Give the Armor a defense level: '))
        armor = Armor(name,defense)
        return armor

    def create_hero(self):
        name = input("Enter a hero name: ")
        health = int(input("Enter starting health: "))
        hero = Hero(name, health)

        choice_armor = input('Would you like to add armors for your hero, Y/N?: ').lower()
        if choice_armor == 'y':
            num = int(input('How many armors? '))
            for i in range(num):
                hero.add_armor(self.create_armor())

        choice_ability = input('Would you like to add abilities for your hero, Y/N?: ').lower()
        if choice_ability == 'y':
            num = int(input('how many abilities?: '))
            for i in range(num):
                hero.add_ability(self.create_ability())

        choice_weapon = input('Would you like to add weapons for your hero, Y/N?: ').lower()
        if choice_weapon == 'y':
            num = int(input('how many weapons?: '))
            for i in range(num):
                hero.add_weapon(self.create_weapon())

        return hero

    def build_team_one(self):
        name = input('enter name for team 1: ')
        team1 = Team(name)
        num_team1 = int(input('how many heroes do you want on your team 1?: '))
        for i in range(num_team1):
            hero1 = self.create_hero()
            team1.add_hero(hero1)
        self.team_one = team1

    def build_team_two(self):
        name = input('enter name for team 2: ')
        team2 = Team(name)
        num_team2 = int(input('how many heroes do you want on your team 2?: '))
        for i in range(num_team2):
            hero2 = self.create_hero()
            team2.add_hero(hero2)
        self.team_two = team2

    def team_battle(self):
        return self.team_one.attack(self.team_two)

    def show_stats(self):
        if len(self.team_one.get_alive()) > 0:
            print(f"{self.team_one.name} wins!")
            for hero in self.team_one.get_alive():
                print(hero)
                print("team one alive")
            #print(self.team_one.get_alive())

        else:
            
            print(f"{self.team_two.name} wins!")
            for hero in self.team_two.get_alive():
                print(hero)
                print("team two alive")
        self.team_one.stats()
        self.team_two.stats()



if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
    # If you run this file from the terminal
    # this block of code is executed.
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # # print(hero.current_health)
    # hero.take_damage(1500)
    # print(hero.is_alive())
    # fire = Ability("Fire",20)
    # hero1 = Hero('Hero1',200)
    # hero1.add_ability(fire)
    # # OOP example printing out objects attribute 
    # print(hero1.abilities[0].name)
    # ability = Ability("Debugging Ability", 20)
    # armor = Armor("Debugging Armor", 10)
    # print(armor.name)
    # print(armor.block())
    # print(ability.name)
    # print(ability.attack())
