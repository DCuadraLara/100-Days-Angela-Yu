class Fuel:
    def __init__(self, name, price_per_liter, available_liters):
        self.name = name
        self.price = price_per_liter
        self.available = available_liters

class FuelMenu:
    def __init__(self):
        self.fuels = [
            Fuel("diesel", 1.70, 500),
            Fuel("gasoline", 1.90, 600),
            Fuel("electric", 0.30, 200)
        ]

    def get_items(self):
        return "/".join([fuel.name for fuel in self.fuels])

    def find_fuel(self, fuel_name):
        for fuel in self.fuels:
            if fuel.name == fuel_name:
                return fuel
        return None
