class aircrafts:
    def __init__(self , type , speed , fuel_capaciti):
        self.type = type
        self.speed = speed
        self.fuel_capaciti = fuel_capaciti

    def __str__(self):
        return f"Type: {self.type}, Speed: {self.speed}, Fuel Capacity: {self.fuel_capacity}"