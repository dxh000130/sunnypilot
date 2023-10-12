import socket
import json

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = ''
    while True:
        packet = s.recv(4096).decode('utf-8')
        if not packet: 
            break
        data += packet

    deserialized_data = json.loads(data)
    print(deserialized_data)
