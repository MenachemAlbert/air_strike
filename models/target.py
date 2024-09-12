class target:
    def __init__(self , city , priority):
        self.city = city
        self.priority = priority

    def __str__(self): return f"city: {self.city}, priority: {self.priority}"