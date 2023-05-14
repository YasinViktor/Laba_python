class Laptop:
    __instance = None

    def __init__(self, model="Macbook", screen_size=16.2, ram=8, storage=315, battery_life=85, battery_level=91):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level

    @staticmethod
    def get_instance():
        if Laptop.__instance is None:
            Laptop.__instance = Laptop()
        return Laptop.__instance

    def add_ram(self, value):
        self.ram += value

    def add_storage(self, value):
        self.storage += value

    def charge(self):
        self.battery_level = 100

    def __str__(self):
        return f"Laptop(model={self.model}, screen_size={self.screen_size}, ram={self.ram}, storage={self.storage}, battery_life={self.battery_life}, battery_level={self.battery_level})"


laptops = [Laptop("Macbook", 16.2, 8, 315, 85, 91), Laptop(), Laptop.get_instance(), Laptop.get_instance()]

for laptop in laptops:
    print(laptop)
