# Lessons:
# - Self
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self

player2 = PlayerCharacter('Tom', 20)
print(player2.run())
