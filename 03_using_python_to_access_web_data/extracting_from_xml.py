
'''

Program for extracting data from an XML file.
In this case we search in an XML containing different comments, each with a count value for this value.
At the end we print the count and sum of these count values.

'''


from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

url = 'http://py4e-data.dr-chuck.net/comments_220607.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml_content = urlopen(url, context=ctx)
xml_data = xml_content.read()
xml_tree = ET.fromstring(xml_data)

print('Retrieved', len(xml_data), 'characters')

# comment_list = xml_tree.findall('comments')[0].findall('comment')
count_value_list = xml_tree.findall('comments/comment/count')

value_list = []

for count in count_value_list:

    # comment_value = int(comment.findall('count')[0].text)
    count_value = int(count.text)
    value_list.append(count_value)

print('Count: {}'.format(len(value_list)))
print('Sum: {}'.format(sum(value_list)))


