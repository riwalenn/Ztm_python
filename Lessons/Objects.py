# Lessons:
# - Objects
# - Attributes and Methods
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def run(self):
        print("run")
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter("Cindy", 38)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50

print(player1.run())
print(player2.name)
print(player2.age)
print(player2.attack)
print(player2.membership)
print(player1.shout())
