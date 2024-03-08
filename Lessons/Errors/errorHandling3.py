# Lessons:
# - Error Handling

while True:
    try:
        age = int(input('Enter your age: '))
        raise ValueError('hey cut it out')
        # raise Exception('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than zero')
        break
    else:
        print('thank you')
    finally:
        print('ok, i am finally done')
    print('can you hear me ?')
