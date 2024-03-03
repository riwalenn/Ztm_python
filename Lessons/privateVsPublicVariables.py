# Lessons:
# - private vs public variables
# add _ before variable : private
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter("Cindy", 38)
# player1.name = '!!!'
# player1.speak = 'BOOOOO'

print(player1.speak())
