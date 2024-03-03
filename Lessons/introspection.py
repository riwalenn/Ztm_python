# Lessons :
# - introspection

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # old call
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)  # new call
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


# introspection
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

print(dir(wizard1))  # use dir() for introspection
