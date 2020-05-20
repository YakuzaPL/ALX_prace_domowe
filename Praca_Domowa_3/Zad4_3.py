class Train():
    def __init__(self, speed=10, fuel_quantity=1000):
        self.speed = speed
        self.fuel_quantity = fuel_quantity

    def description(self):
        return f"Moja prędkość to: {self.speed}km/h, ilość paliwa to: {self.fuel_quantity}l"

    def __str__(self):
        return self.description()

    def speed_up(self, new_speed):

        old_speed = self.speed
        self.speed = new_speed
        if new_speed >= old_speed * 1.75:
            self.speed = old_speed
        elif self.fuel_quantity <= 0:
            self.speed = old_speed
        else:
            fuel_usage = (self.speed * old_speed) * (old_speed/100)
            old_fuel = self.fuel_quantity
            self.fuel_quantity = old_fuel - fuel_usage


train = Train()
train.speed_up(15)

print(train)
