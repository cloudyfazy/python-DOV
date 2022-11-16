from telnetlib import GA
class Vehicle:
    # class attribute
    color = 'white'
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.mileage = milage
    def seating_capacity(self, capacity=50):
        self.capacity = capacity
        return f"Seating capacity {capacity}"
    def fare(self):
        pass