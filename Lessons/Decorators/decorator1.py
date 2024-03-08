# Lessons:
# - decorator


def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')

    return wrap_func


@my_decorator
def hello():
    print("helloooo")


@my_decorator
def bye():
    print("see ya later")


hello()
bye()

# Underneath the hood, what decorator is doing ?
# hello2 = my_decorator(hello)
# hello2()
# my_decorator(hello)()
