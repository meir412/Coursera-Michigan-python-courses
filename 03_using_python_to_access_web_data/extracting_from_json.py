
from urllib.request import urlopen
import json

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'

url = 'http://py4e-data.dr-chuck.net/comments_220608.json'

# url = input('Enter location: ')

print('Retrieving {}'.format(url))

data_in_unicode = urlopen(url).read()

print('Retrieved', len(data_in_unicode), 'characters')

data_as_dict = json.loads(data_in_unicode)

value_list = []

for comment in data_as_dict['comments']:

    comment_value = int(comment['count'])
    value_list.append(comment_value)



print('Count: {}'.format(len(value_list)))
print('Sum: {}'.format(sum(value_list)))

