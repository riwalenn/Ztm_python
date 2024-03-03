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

    def run(self):
        return self

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter("Cindy", 38)
print(PlayerCharacter.adding_things(3, 4))

player2 = PlayerCharacter('Tom', 20)
print(player2.run())
