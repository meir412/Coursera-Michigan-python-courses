
# A program that finds the most common word and the num. of times it appeared in a text file of the user's choice
# Use the file name mbox-short.txt as the file name

file_name = input('Enter file name: ')

try:

    file_handler = open(file_name)
    mail_count = dict()

    for line in file_handler:

        if line.startswith('From '):

            line_list = line.split()
            mail = line_list[1]
            mail_count[mail] = mail_count.get(mail, 0) + 1

    most_common_mail = None
    most_common_count = None

    for mail, count in mail_count.items():

        if (most_common_count is None) or (count > most_common_count):

            most_common_mail = mail
            most_common_count = count


    print(most_common_mail, most_common_count)

except:

    print('Sorry, but no file by the name of %s exists here' % file_name)
