from models.abstract_laptop import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    def __init__(self, model, screenSize, ram, storage, batteryLife, batteryLevel, gpu, fans):
        super().__init__(model, screenSize, ram, storage, batteryLife, batteryLevel)
        self.gpu = gpu
        self.fans = fans

    def replaceBattery(self, capacityInHours):
        print("Replacing battery for Gaming Laptop...")
        self.batteryLife = capacityInHours
        self.batteryLevel = 90

    def __str__(self):
        return f"--- Gaming Laptop ---\n{super().__str__()}\nGPU: {self.gpu}\nFans: {self.fans}"