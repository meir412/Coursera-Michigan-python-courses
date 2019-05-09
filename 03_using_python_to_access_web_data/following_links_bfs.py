
'''

Program for extracting and following links using urlib and beautifulsoup.
The program receives an initial url, a count and a position from the user. It then searches for the link at the users
desired position and opens it's url. The program repeats this process as many times as the users desired count.


* These are the values to test yourself:

    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    count = 4
    position = 3

'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

html_content = urlopen(url, context=ctx).read()
html_parser = BeautifulSoup(html_content, "html.parser")
print('Retrieving: {}'.format(url))

for i in range(count):

    url = html_parser.find_all('a')[position - 1].get('href')
    html_content = urlopen(url, context=ctx).read()
    html_parser = BeautifulSoup(html_content, "html.parser")
    print('Retrieving: {}'.format(url))
