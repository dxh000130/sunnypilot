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
        
        # 尝试反序列化 JSON
        try:
            deserialized_data = json.loads(data)
            print(deserialized_data)
            # 清除缓冲区以便接收新的 JSON 数据
            data = ''
        except json.JSONDecodeError:
            # 如果反序列化失败，则打印原始数据
            print("Incomplete JSON:", data)

