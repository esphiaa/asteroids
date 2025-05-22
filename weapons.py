class Weapon:
    def __init__(self, name, cooldown, color):
        self.name = name
        self.cooldown = cooldown
        self.color = color

    def __str__(self):
        return f"{self.name}, Cooldown: {self.cooldown}"
    
basic_laser = Weapon("Basic Laser", 0.75, "white")
advanced_laser = Weapon("Advanced Laser", 0.5, "blue")
plasma_cannon = Weapon("Plasma Cannon", 0.25, "red")
orbital_ray = Weapon("Orbital Ray", 0.1, "pink")

weapons = [basic_laser, advanced_laser, plasma_cannon, orbital_ray]