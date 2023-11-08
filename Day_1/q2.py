# **_Write a program which can compute the factorial of a given
# numbers.The results should be printed in a comma-separated sequence
# on a single line.Suppose the following input is supplied to the
# program: 8
# Then, the output should be:40320_**
from functools import reduce
import math


def main():
    user_num = int(input('Provide number: '))
    print(math.factorial(user_num))


if __name__ == '__main__':
    main()
num = 8


def fun(acc, i):
    return acc * i


print(reduce(fun, range(1, num + 1)))

fact = 1

for i in range(1, num + 1):
    fact = fact * i
    print(fact)