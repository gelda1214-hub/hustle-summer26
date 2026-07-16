
import random
from armor import Armor
from ability import Ability
class Hero:
  
    def __init__(self, name, starting_health=100):
    
    
     self.name = name
     self.starting_health = starting_health
     self.current_health = starting_health
     self.abilities = []
     self.armor = []

    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list) )
    def add_ability(self, ability):
        self.ability = ability

    def attack(self):
       total_damage = 0
       for ability in self.ability:
            total_damage += ability.attack()
       print(total_damage)
       return total_damage
    
    def add_armor(self, armor):
        self.armor.append(armor)
   
    def defend(self):
        total_defense = 0
        for armor in self.armor:
            total_defense += armor.block()
        return total_defense
    
    def take_damage(self, damage):
        blocked = self.defend()
        damage_taken = max(0, damage - blocked)
        self.current_health -= damage_taken
        if self.current_health < 0:
            self.current_health = 0
        return damage_taken
 
if __name__ == "__main__":
     my_hero = Hero("Myles Morales", 200)
#print(my_hero.name)
#print(my_hero.current_health)
#my_opponent = Hero("Green Goblin", 150)
#my_hero.battle(my_opponent)
#my_hero.add_ability(Ability("Web Slinging", 25))
#my_hero.add_ability(Ability("Spider Sense", 10))
#my_hero.attack()
my_hero.add_armor(Armor("Gloves", 5))
my_hero.add_armor(Armor("A Really Cool Hat", 10))
# my_hero.defend()
my_hero.take_damage(10)
