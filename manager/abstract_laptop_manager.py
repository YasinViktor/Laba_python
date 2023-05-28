"""
Module: abstract_laptop_manager
"""

from models.business_laptop import BusinessLaptop
from models.convertible_laptop import ConvertibleLaptop
from models.gaming_laptop import GamingLaptop
from models.ultrabook import Ultrabook

laptops = [
    GamingLaptop("ASUS ROG", 15.6, 16, 1000, 5, 70, "Nvidia GTX 3080", 3),
    Ultrabook("Dell XPS 13", 13.4, 8, 512, 12, 90, 2.8, 0.58),
    GamingLaptop("Acer Predator Helios", 17.3, 32, 2000, 4, 60, "AMD Radeon RX 6800M", 5),
    Ultrabook("HP Spectre x360", 14, 16, 1, 16, 95, 2.87, 0.67),
    ConvertibleLaptop("Microsoft Surface Laptop", 13.5, 1, 512, 65, 80, "Surface Pen", True),
    BusinessLaptop("Dell Latitude 9420", 14, 16, 256, 16, 45, "Intel Core i5 ", True)
]


def find_laptops_with_screen_greater_than(laptops, screen_size):
    """
    Find laptops with screen size greater than the specified value.
    """
    return [laptop for laptop in laptops if laptop.screen_size > screen_size]


def find_gaming_laptops_with_fans_greater_than(laptops, fans):
    """
    Find gaming laptops with fans greater than the specified value.
    """
    return [laptop for laptop in laptops if isinstance(laptop, GamingLaptop) and laptop.fans > fans]


if __name__ == "__main__":
    for laptop in laptops:
        print(laptop)
        laptop.replace_battery(10)
        print("After battery replacement:", laptop)

    laptops_with_screen_greater_than_15 = find_laptops_with_screen_greater_than(laptops, 15)
    print("Laptops with screen size greater than 15:")
    for laptop in laptops_with_screen_greater_than_15:
        print(laptop)

    gaming_laptops_with_fans_greater_than_2 = find_gaming_laptops_with_fans_greater_than(laptops, 2)
    print("Gaming laptops with fans greater than 2:")
    for laptop in gaming_laptops_with_fans_greater_than_2:
        print(laptop)
