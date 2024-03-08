# Lessons:
# - Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter two numbers  {err}')


print(sum(1, 2))


def sum2(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum2(1, 0))
