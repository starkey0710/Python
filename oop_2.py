class Character:
    def __init__(self, h, n):
        self.health = h
        self.name = n
    def __str__(self):
        healthInfo = "Health: " + str(self.health)
        nameInfo = "Name: " + str(self.name)
        return nameInfo + " " + healthInfo
    def changeName(self, newName):
        self.name = newName
    def eat(self):
        self.health = self.health + 5
    def attack(self, otherPlayer):
        otherPlayer.health = otherPlayer.health - 5

player1 = Character(50, "frank")
player2 = Character(50, "bob")

print(player2)


player1.attack(player2)
print(player2)

player1.eat()
print(player1)
