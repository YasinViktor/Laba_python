from models.abstract_laptop import AbstractLaptop


class Ultrabook(AbstractLaptop):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level, weight, thickness):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.weight = weight
        self.thickness = thickness

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    def __str__(self):
        return f"--- Ultrabook ---\n{super().__str__()}\nWeight: {self.weight} kg\nThickness: {self.thickness} cm"