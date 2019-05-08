"""

use http://py4e-data.dr-chuck.net/comments_42.html
or http://py4e-data.dr-chuck.net/comments_220605.html

"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/comments_220605.html'
html_content = urlopen(url, context=ctx).read()
html_parser = BeautifulSoup(html_content, "html.parser")


all_spans = html_parser('span')
comment_value_list = []

for span_object in all_spans:

    current_span = span_object.contents[0]

    # TODO: validate it's actually an integer
    comment_value = int(current_span)

    comment_value_list.append(comment_value)
    print(comment_value)

print(sum(comment_value_list))

