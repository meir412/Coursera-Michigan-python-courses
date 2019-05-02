
# This program is built for text files that are in the format of the mbox-short.txt example file from py4e.
# It finds the relevant lines of text for records, finds the hour of the day of the record, and prints the hours and
# their frequencies sorted by the hour of the day.
# Use the file name mbox-short.txt as the file name (for the py4e autograder)

file_name = input('Enter file name: ')

try:

    if len(file_name) < 1:
        file_handler = open('mbox-short.txt')  # allowing the user to just press enter and get the mbox file
    else:
        file_handler = open(file_name)

    hour_frequency_db = dict()

    for line in file_handler:

        if line.startswith('From '):

            line_list = line.split()
            date = line_list[5]
            hour = date.split(sep=':')[0]
            hour_frequency_db[hour] = hour_frequency_db.get(hour,0) + 1

    # most_common_hour = None         # this code can sort the pairs by the frequency and not by the hour
    # most_common_count = None        # might come in handy
    # item_list = []
    #
    # for hour, count in hour_frequency_db.items():
    #
    #     item_list.append((count, hour))
    #
    # sorted_item_list = sorted(item_list, reverse=True)

    item_list = list(hour_frequency_db.items())
    sorted_item_list = sorted(item_list)


    for hour, count in sorted_item_list:
        print(hour, count)

except:

    print('Sorry, but no file by the name of %s exists here' % file_name)
