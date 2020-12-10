
class Weapon:
    def __init__(self, damage=20, ammo=5):
        self.damage = damage
        self.ammo = ammo

    def attack(self):
        return self.damage

    def reload(self):
        if self.ammo < 5:
            self.ammo = 5
            return "Reloaded."
        else:
            return "Ammo full."