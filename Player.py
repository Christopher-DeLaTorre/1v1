from Weapon import Weapon

class Player:
    def __init__(self, name="_____", weapon=Weapon(), health=100):
        self._health = health
        self.weapon = weapon
        self.name = name 

    def change_name(self, name):
        self.name = name 

    def get_name(self):
        return self.name

    def lose_health(self):
        self._health -= self.weapon.attack()

    def change_weapon(self, damage, ammo):
        self.weapon.damage = damage
        self.weapon.ammo = ammo

    