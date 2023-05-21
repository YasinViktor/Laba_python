from abc import ABC, abstractmethod

class AbstractLaptop(ABC):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level

    @abstractmethod
    def replace_battery(self, capacity_in_hours):
        pass
