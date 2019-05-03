
# solution for 1st assignment in the 3rd "python for everybody" course

# testing with "regex_sum_42.txt" data file

import re

file_name = input('Enter file name: ')

try:

    if len(file_name) < 1:
        file_handler = open('regex_sum_42.txt')  # allowing the user to just press enter and get the regex file
    else:
        file_handler = open(file_name)

    number_list = []

    for line in file_handler:

        numbers_in_line = re.findall('[0-9]+', line)    # creates a list of strings representing numbers in the line

        if len(numbers_in_line) == 0:    # if the list is empty, no need to add numbers to the number list
            continue

        for number in numbers_in_line:  # for each string in the lines list, convert to integer and add to number list

            number_list.append(int(number))

    print(sum(number_list))


except FileNotFoundError:

    print('Sorry, but no file by the name of %s exists here' % file_name)


# And this is how to solve the problem in one line, excluding the file name validation:
# print(sum([int(number) for number in re.findall('[0-9]+', open(input('Enter file name: ')).read())]))