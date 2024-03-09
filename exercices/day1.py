# Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


def question_1(start, end):
    for i in range(start, end):
        if (i % 7 == 0) and (i % 5 != 0):
            yield i


for i in question_1(2000, 3201):
    print(i, end=",")  # sep="," fait un retour à la ligne à la place

print("\b")

# print(*(i for i in question_1(2000, 3201)), sep=",")

# Question 2
# Write a program which can compute the factorial of a given numbers.The results should be printed in a
# comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8
# Then, the output should be:40320

# Question 3
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36,
# 7: 49, 8: 64}
