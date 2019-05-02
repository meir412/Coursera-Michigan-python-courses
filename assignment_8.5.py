# Use the file name mbox-short.txt as the file name

file_name = input('Enter file name: ')

try:
    file_handler = open(file_name)
    from_count = 0

    for line in file_handler:

        if line.startswith('From '):

            line_list = line.split()
            print(line_list[1])
            from_count = from_count + 1

    print('There were %d lines in the file with From as the first word' % from_count)

except:
    print('Sorry, but no file by the name of %s exists here' % file_name)
