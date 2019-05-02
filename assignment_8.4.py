# Use the file name romeo.txt as the file name

file_name = input('Enter file name: ')

try:
    file_handler = open(file_name)
    word_list = []

    for line in file_handler:

        line_words = line.split()

        for word in line_words:

            if word not in word_list:

                word_list.append(word)

    word_list.sort()
    print(word_list)

except:
    print('Sorry, but no file by the name of %s exists here' % file_name)
