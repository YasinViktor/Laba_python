"""main"""
from manager.abstract_laptop_manager import LaptopManager
from models.business_laptop import BusinessLaptop
from models.convertible_laptop import ConvertibleLaptop
from models.gaming_laptop import GamingLaptop
from models.ultrabook import Ultrabook

if __name__ == "__main__":
    laptops = [
        GamingLaptop("ASUS ROG", 15.6, 16, 1000, 5, 70, "Nvidia GTX 3080", 3),
        Ultrabook("Dell XPS 13", 13.4, 8, 512, 12, 90, 2.8, 0.58),
        GamingLaptop("Acer Predator Helios", 17.3, 32, 2000, 4, 60, "AMD Radon RX 6800M", 5),
        Ultrabook("HP Spectre x360", 14, 16, 1, 16, 95, 2.87, 0.67),
        ConvertibleLaptop("Microsoft Surface Laptop", 13.5, 1, 512, 65, 80, "Surface Pen", True),
        BusinessLaptop("Dell Latitude 9420", 14, 16, 256, 16, 45, "Intel Core i5", True)
    ]

    manager = LaptopManager(laptops)
    enumerated = manager.get_enumerated()
    # combined_results = manager.get_combined_results()
    attributes_by_type = manager.get_attributes_by_type(int)
    condition_result = manager.check_condition(60)
    # print(manager.replace_battery_if_needed(55))

    for laptop_item in manager:
        print(laptop_item)
    for laptop_item in laptops:
        print(laptop_item.vocabulary(str))

    print(condition_result)
