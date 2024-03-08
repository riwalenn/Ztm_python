# Lessons:
# - Error Handling

while True:
    try:
        age = int(input('Enter your age: '))
    except ValueError:
        print('please enter an number')
    except ZeroDivisionError:
        print('please enter age higher than zero')
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done')
