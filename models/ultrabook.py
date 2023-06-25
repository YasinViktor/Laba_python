from models.abstract_laptop import AbstractLaptop


class Ultrabook(AbstractLaptop):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level, weight, thickness):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.weight = weight
        self.thickness = thickness
        self.favorite_food_set = {"pizza", "chocolate"}

    def replace_battery(self, capacity_in_hours):
        print("Battery replacement is not possible for Ultrabooks.")


    def __str__(self):
        return f"--- Ultrabook ---\n{super().__str__()}\nWeight: {self.weight} kg\nThickness: {self.thickness} cm"

