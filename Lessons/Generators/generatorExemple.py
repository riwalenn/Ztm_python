# Lessons:
# - Generators
# - Generators are iterable

def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)
print(my_list)


# Generator

def generator_function(num):
    for i in range(num):
        yield i * 2


my_generator = generator_function(10)
next(my_generator)  # return 0
next(my_generator)  # return 2
print(next(my_generator))  # return 4
