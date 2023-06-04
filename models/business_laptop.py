from models.abstract_laptop import AbstractLaptop


class BusinessLaptop(AbstractLaptop):
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level, processor, fingerprint_scanner):
        super().__init__(model, screen_size, ram, storage, battery_life, battery_level)
        self.processor = processor
        self.fingerprint_scanner = fingerprint_scanner

    def replace_battery(self, capacity_in_hours):
        self.battery_life = capacity_in_hours

    def do_something(self):
        return "Business laptop does something."

    def __str__(self):
        return f"--- Business Laptop ---\n{super().__str__()}\nProcessor: {self.processor}\n" \
               f"Fingerprint Scanner: {self.fingerprint_scanner}"
