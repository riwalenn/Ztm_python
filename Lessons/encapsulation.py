# Lessons:
# - Encapsulation
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter("Cindy", 38)
print(player1.speak())

# Dictionary if I just want data
player2 = {'name': 'Tess', 'age': '45'}
print(player2['name'])
print(player2['age'])
