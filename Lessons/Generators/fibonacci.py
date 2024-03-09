# Lessons:
# - Generators
# - Exercice Fibonacci numbers


def fibonacci_generator(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


for item in fibonacci_generator(21):
    print(item)
