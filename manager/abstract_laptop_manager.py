class LaptopManager:
    def __init__(self, laptops):
        self.laptops = laptops

    def __len__(self):
        return len(self.laptops)

    def __getitem__(self, index):
        return self.laptops[index]

    def __iter__(self):
        return iter(self.laptops)

    def do_something_for_all_laptops(self):
        return [laptop.do_something() for laptop in self.laptops]

    def enumerate_laptops(self):
        return [(index, laptop) for index, laptop in enumerate(self.laptops)]

    def zip_laptops_with_do_something(self):
        return zip(self.laptops, self.do_something_for_all_laptops())

    def get_attributes_by_data_type(self, data_type):
        return {laptop: laptop.get_attributes_by_type(data_type) for laptop in self.laptops}

    def all_any_check(self, condition):
        return {"all": all(condition(laptop) for laptop in self.laptops),
                "any": any(condition(laptop) for laptop in self.laptops)}
