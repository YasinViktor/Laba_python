import logging


class RedundantChargeException(Exception):
    pass


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    logging.error(str(e))
                elif mode == 'file':
                    logging.basicConfig(filename='log.txt', level=logging.ERROR)
                    logging.error(str(e))
                else:
                    raise ValueError("Invalid logging mode. Choose 'console' or 'file'.")

        return wrapper

    return decorator


class AbstractLaptop:
    def __init__(self, model, screen_size, ram, storage, battery_life, battery_level):
        self.model = model
        self.screen_size = screen_size
        self.ram = ram
        self.storage = storage
        self.battery_life = battery_life
        self.battery_level = battery_level

    @logged(RedundantChargeException, 'console')
    def charge(self):
        if self.battery_level == 100:
            raise RedundantChargeException("The laptop is already fully charged.")
        else:
            self.battery_level = 100
            print("The laptop is now fully charged.")

    def get_attributes_by_type(self, data_type):
        return {attr: value for attr, value in self.__dict__.items() if isinstance(value, data_type)}

    def __str__(self):
        return f"--- Abstract Laptop ---\nModel: {self.model}\nScreen Size: {self.screen_size}\n" \
               f"RAM: {self.ram} GB\nStorage: {self.storage} GB\nBattery Life: {self.battery_life} hours\n" \
               f"Battery Level: {self.battery_level}%"
