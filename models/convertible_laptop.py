from models.abstract_laptop import AbstractLaptop


class ConvertibleLaptop(AbstractLaptop):
    def __init__(self, model, screenSize, ram, storage, batteryLife, batteryLevel, pen, touchScreen):
        super().__init__(model, screenSize, ram, storage, batteryLife, batteryLevel)
        self.pen = pen
        self.touchScreen = touchScreen

    def replaceBattery(self, capacityInHours):
        self.batteryLevel = capacityInHours

    def __str__(self):
        return f"--- Convertible Laptop ---\n{super().__str__()}\nPen: {self.pen}\nTouch Screen: {self.touchScreen}"