import socket

BUFFSIZE = 4096
SERVER_IP = '127.0.0.1' 
SERVER_PORT = 5000 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((SERVER_IP, SERVER_PORT))

headers = """\
POST {url} HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
\r\n"""

body = 'username=mariofafaf&password=rossi'                                 
header_string = headers.format(
    url="http://127.0.0.1:5000/",
    content_type="application/x-www-form-urlencoded",
    content_length=len(body),
    host=str(SERVER_IP) + ":" + str(SERVER_PORT)
)

payload = header_string + body

s.sendall(payload.encode())

data = s.recv(BUFFSIZE)
while data != b'':
    print(data)
    data = s.recv(BUFFSIZE)

s.close() 