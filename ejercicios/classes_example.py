
class Weapon:

    def __init__(self, name: str, damage: int, durability: int, weapon_type: str):
        self.name = name
        self.damage = damage
        self.durability = durability

    def repair(self):
        self.durability += 1

class Person:
    
    def __init__(self, name: str, age: int, weapon: Weapon):
        self.name = name
        self.age = age
        self.weapon = weapon
        self.hp = 100

    def catch_phrase(self):
        return "Dale mono"

    def hit_points(self):
        return self.hp

    def attack(self):
        self.weapon.durability -= 1
        # mas hueas pasan o_o
        pass

rusty_sword = Weapon("Rusty Sword", 2, 5, "Melee")
broken_wand = Weapon("Broken Wand", 1, 10, "Ranged")

matigol = Person("Matigol", 23, rusty_sword)
dodi = Person("Dodi", 23, broken_wand)
elmer = Person("Elmer", 24, rusty_sword)
clemente = Person("Clemente", 23, rusty_sword)
dodi_clone = Person("Dodi Clone", 10, broken_wand)
future_dodi = Person("Future Dodi", 30, broken_wand)

crew = [matigol, dodi, elmer, clemente, dodi_clone, future_dodi]



