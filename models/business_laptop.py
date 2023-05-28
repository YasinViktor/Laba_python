from models.abstract_laptop import AbstractLaptop


class BusinessLaptop(AbstractLaptop):
    def __init__(self, model, screenSize, ram, storage, batteryLife, batteryLevel, processor, fingerprintScanner):
        super().__init__(model, screenSize, ram, storage, batteryLife, batteryLevel)
        self.processor = processor
        self.fingerprintScanner = fingerprintScanner

    def replaceBattery(self, capacityInHours):
        self.batteryLife = capacityInHours

    def __str__(self):
        return f"--- Business Laptop ---\n{super().__str__()}\nProcessor: {self.processor}\nFingerprint Scanner: {self.fingerprintScanner}"






