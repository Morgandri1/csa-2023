#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#
#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"GET_KEY")
    data = s.recv(1024).decode()[::-1]
    s.send(data.encode())
    data = s.recv(1024).decode()

print(f"Received {data}")
