from models.abstract_laptop import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level, gpu, fans):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.gpu = gpu
        self.fans = fans

    def replace_battery(self, capacity_in_hours):
        print("Replacing battery for Gaming Laptop...")
        self.battery_life = capacity_in_hours
        self.battery_level = 90

    def __str__(self):
        return f"--- Gaming Laptop ---\n{super().__str__()}\nGPU: {self.gpu}\nFans: {self.fans}"
