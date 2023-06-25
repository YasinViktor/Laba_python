from models.abstract_laptop import AbstractLaptop


class ConvertibleLaptop(AbstractLaptop):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level, pen, touch_screen):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.pen = pen
        self.touch_screen = touch_screen
        self.favorite_food_set = {"worms", "grain"}

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    def do_something(self):
        return "Convertible laptop does something."

    def __str__(self):
        return f"--- Convertible Laptop ---\n{super().__str__()}\nPen: {self.pen}\nTouch Screen: {self.touch_screen}"
