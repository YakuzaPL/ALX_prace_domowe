class Container:
    def __init__(self, water_quantity):
        self.water_quantity = water_quantity

    def pour(self, how_much):
        self.water_quantity = self.water_quantity + how_much
        return self.water_quantity

    def pour_out(self, how_much):
        self.water_quantity = self.water_quantity - how_much
        if self.water_quantity <= 0:
            self.water_quantity = 0
            return self.water_quantity

    def get_info(self):
        if self.water_quantity > 0:
            return f"zbiornik z {self.water_quantity} litrami wody."
        elif self.water_quantity <= 0:
            return "zbiornik jest pusty."
        else:
            return "Better get a bucket"

    def __str__(self):
        return self.get_info()


# i wysypałem się z fizyki...

containter = Container(25)
containter.pour(5)

containter.pour_out(20)


print(containter.get_info())
