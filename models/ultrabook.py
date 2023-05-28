from models.abstract_laptop import AbstractLaptop


class Ultrabook(AbstractLaptop):
    def __init__(self, model, screenSize, ram, storage, batteryLife, batteryLevel, weight, thickness):
        super().__init__(model, screenSize, ram, storage, batteryLife, batteryLevel)
        self.weight = weight
        self.thickness = thickness

    def replaceBattery(self, capacityInHours):
        print("Battery replacement is not possible for Ultrabooks.")

    def __str__(self):
        return f"--- Ultrabook ---\n{super().__str__()}\nWeight: {self.weight} kg\nThickness: {self.thickness} cm"