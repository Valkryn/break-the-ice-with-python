# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# def main():
#     numbers = range(2000, 3200)
#     filtered_numbers = filter_numbers(numbers)
#     print(filtered_numbers)
#
#
# def filter_numbers(lst):
#     filtered_numbers = []
#     for number in lst:
#         if number % 7 == 0 and number % 5 != 0:
#             filtered_numbers.append(number)
#     return filtered_numbers
#
#
def main():
    numbers = list(range(2000, 3200))
    lst = list(filter(filter_range, numbers))
    print(lst)


def filter_range(num):
    return num % 7 == 0 and num % 5 != 0


if __name__ == '__main__':
    main()
