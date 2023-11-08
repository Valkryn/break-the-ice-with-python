# With a given integral number n, write a program to generate a dictionary that
# contains (i, i x i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
from functools import reduce


def main():
    number = int(input('Please provide a number: '))
    new_dict = {}
    for i in range(1, number + 1):
        new_dict[i] = i ** 2
    print(new_dict)


if __name__ == '__main__':
    main()
numm = 8
new_dict = {}


def fun(acc, i):
    new_dict[i] = i ** 2


reduce(fun, range(1, numm + 1),0)

print(new_dict)
