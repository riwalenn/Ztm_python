# Lessons:
# - Objects
# - Attributes and Methods
# - Init
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter("Cindy", 38)
print(player1.shout())
