# Use the file name mbox-short.txt as the file name

file_name = input('Enter file name: ')

try:
    file_handler = open(file_name)

    total = 0
    number_of_lines = 0

    for line in file_handler:

        if not line.startswith('X-DSPAM-Confidence:'):
            continue

        confidence_value = line[line.find(':')+2:]
        confidence_value = float(confidence_value)
        total = total + confidence_value
        number_of_lines = number_of_lines + 1

    average_conf = total/number_of_lines
    print('Average spam confidence:', average_conf)

except:
    print('Sorry, but no file by the name of %s exists here' % file_name)
