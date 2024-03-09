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


for item in generator_function(10):
    print(item)

my_generator = generator_function(10)
next(my_generator)  # return 0
next(my_generator)  # return 2
print(next(my_generator))  # return 4

# see my_decorator exemple, generators a really useful when calculing large sets of data
# particulary if we're using long loops where we don't really want to store that memory
# and we don't need to calculate everything at the same time, maybe one by one.
