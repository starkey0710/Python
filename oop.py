class Bus:
    def __init__(self, n, w, c, s):
        self.name = n
        self.wheels = w
        self.color = c
        self.speed = s
    def __str__(self):
        nameInfo = "Name: " + (self.name)
        wheelInfo = "Wheels: " + str(self.wheels)
        colorInfo = "Color: " + self.color
        speedInfo = "Speed: " + str(self.speed)
        return nameInfo + " " + wheelInfo + " " + colorInfo + " " + speedInfo
    def speedItUp(self):
        self.speed = self.speed + 5
    def changeTheColor(self, newColor):
        self.color = newColor

our_bus = Bus("Hello", 6, "pink", 60)
print(our_bus)
our_bus.speedItUp()
print(our_bus)
our_bus.changeTheColor("blue")
print(our_bus)
