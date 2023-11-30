#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#
import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"ls -a /tmp")
    data = s.recv(1024)

print(f"Received {data!r}")
