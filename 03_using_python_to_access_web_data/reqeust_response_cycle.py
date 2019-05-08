"""
solution for the 2nd assignment in the 3rd "python for everybody" course.
This assignment is handed out after studying networks and socket, and the HTTP request response cycle.
The solution uses the `socket` module which is used to send messages across a network with python.

The program prompts the user for a file name and then connects to the domain 'data.pr4e.org' on port 80. Then, the program
sends an HTTP GET request 'data.pr4e.org/{users file name}.txt and receives and prints the response it returns. If the
response is a 404-not-found error, the program prints a message stating that no file by the name the user specified is
found on the page.

The way it works is by using a socket from the socket module which connects to the address and port specified above.
The socket then sends a predefined and encoded HTTP GET command requesting the address/users_chosen name.txt .
Than an loop starts, that will go no until reaching break. At the beggining of each iteration the socket receives
from the address in chunks of 512 characters and stores the bytes in the 'data' variable. if 'data' is empty, the loop
simply breaks. If it isn't empty, a test is run - the data is split (into bytes that represent words), if the second byte
represents the word '404' (which means that the response was a 404 not found), the 'not found' message is printed to the
user, and the loop is terminated. If not, the data is decoded to a string and printed, and the loop iterates again and
again, until the response is over and data is empty.
After the loop is terminated, the socket is disconnected and the program ends.

You can test this program by entering 'intro-short' or any other file name that appears on 'data.py4e.org'
On the py4e autograder I was asked to insert some of the parameters received in the header of the HTTP response
received after requesting 'data.py4e.org/intro-short.txt'.
"""

import socket

file_name = input('Enter file name: ')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/{}.txt HTTP/1.0\r\n\r\n'.format(file_name).encode()
mysock.send(cmd)

while True:

    data = mysock.recv(512)

    if len(data) < 1:
        break

    if data.split()[1].decode() == "404":
        print('Sorry, but no file by the name of {} exists on our page'.format(file_name))
        break

    print(data.decode(), end='')


mysock.close()
