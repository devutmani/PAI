class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculateFare(self):
        return self.capacity*100

class Bus(Vehicle):
    def __ini__(self, capacity):
        super().__init__(capacity)

    def fare(self):
        totalFare = super().calculateFare()
        totalFare += totalFare*0.10
        return totalFare

b = Bus(20)
busFare = b.fare()
print(f"Bus Capacity: {b.capacity}")
print(f"Bus fare: {busFare}")