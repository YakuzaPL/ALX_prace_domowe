class Tortoise:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def go(self, move):
        if self.z == 0:
            self.y = self.y - move
        elif self.z == 90:
            self.x = self.x + move
        elif self.z == 180:
            self.y = self.y + move
        elif self.z == 270:
            self.x = self.x + move

    def turn(self, turn):
        self.z = self.z + turn
        if self.z >= 270:
            self.z = 0

    def geto_info(self):
        return f"x={self.x}, y={self.y}"

    def __str__(self):
        return self.geto_info()


tortois = Tortoise(100, 100)
tortois.go(50)
print(tortois.geto_info())
tortois.turn(90)
tortois.go(50)
print(tortois.geto_info())



