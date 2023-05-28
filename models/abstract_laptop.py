from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level
        self.favorite_food_set = set()

    @abstractmethod
    def replace_battery(self, capacity_in_hours):
        pass

    def get_attributes_by_type(self, data_type):
        return {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}

    def __str__(self):
        return f"--- Abstract Laptop ---\nModel: {self.model}\nScreen Size: {self.screen_size}\n" \
               f"RAM: {self.ram} GB\nStorage: {self.storage} GB\nBattery Life: {self.battery_life} hours\n" \
               f"Battery Level: {self.battery_level}%"
