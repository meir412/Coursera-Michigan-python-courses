
"""
solution for the 1st assignment in the 3rd "python for everybody" course.
This assignment is handed out after studying regular expressions.
The solution uses the `re` module which adds regexp functionality to python

The program prompts the user for a text file name and then searches for integers inside the text.
The program then computes and prints the sum of these integers.

The way it works is by using a file handler (output of the open function) and iterating over its rows.
For each row, a list of strings that represents integers is created using the regexp `findall` function.
Then each string is parsed into an integer and added to a larger list of integers from all of the lines.
At the end the sum of this list is computed and printed.

At the end of the file there is a commented out line that represents a super short and confusing solution.
The short solution uses list comprehension and the file handler's read method which extracts all of the text at once.

You need to test this assignment twice:
Once with the `regex_sum_42.txt` (which will be the default file chosen if the user presses enter)
And the second time with `regex_sum_?????.txt` - a unique generated text that each student receives.
"""


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