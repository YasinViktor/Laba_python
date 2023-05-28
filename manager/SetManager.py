from manager.abstract_laptop_manager import LaptopManager
from models.business_laptop import BusinessLaptop
from models.convertible_laptop import ConvertibleLaptop
from models.gaming_laptop import GamingLaptop
from models.ultrabook import Ultrabook


class SetManager:
    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        return iter(self._get_combined_set())

    def __len__(self):
        return len(self._get_combined_set())

    def __getitem__(self, index):
        return list(self._get_combined_set())[index]

    def __next__(self):
        return next(iter(self._get_combined_set()))

    def _get_combined_set(self):
        combined_set = set()
        for laptop in self.regular_manager:
            combined_set.update(laptop.favorite_food_set)
        return combined_set


laptops = [
    GamingLaptop("ASUS ROG", 15.6, 16, 1000, 5, 70, "Nvidia GTX 3080", 3),
    Ultrabook("Dell XPS 13", 13.4, 8, 512, 12, 90, 2.8, 0.58),
    GamingLaptop("Acer Predator Helios", 17.3, 32, 2000, 4, 60, "AMD Radeon RX 6800M", 5),
    Ultrabook("HP Spectre x360", 14, 16, 1, 16, 95, 2.87, 0.67),
    ConvertibleLaptop("Microsoft Surface Laptop", 13.5, 1, 512, 65, 80, "Surface Pen", True),
    BusinessLaptop("Dell Latitude 7410", 14, 16, 512, 14, 75, "Intel i7", True),
]

laptop_manager = LaptopManager(laptops)
set_manager = SetManager(laptop_manager)

# Level 1
print(f"Number of laptops: {len(laptop_manager)}")
print(f"Laptop at index 2: {laptop_manager[2]}")

print("Iterating over laptops:")
for laptop in laptop_manager:
    print(laptop)

print("Calling do_something() for all laptops:")
print(laptop_manager.do_something_for_all_laptops())

print("Enumerating laptops:")
print(laptop_manager.enumerate_laptops())

print("Zipping laptops with do_something():")
for item in laptop_manager.zip_laptops_with_do_something():
    print(item)

print("Getting attributes by data type:")
print(laptop_manager.get_attributes_by_data_type(int))

print("Checking all and any:")
print(laptop_manager.all_any_check(lambda laptop: laptop.battery_level > 70))

# Level 2
print("Iterating over the combined set of favorite foods:")
for food in set_manager:
    print(food)

print(f"Number of favorite foods: {len(set_manager)}")
print(f"Favorite food at index 1: {set_manager[1]}")

print("Iterating over the combined set using next():")
print(next(set_manager))
print(next(set_manager))
