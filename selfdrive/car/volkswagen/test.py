import socket
import json

def log_and_print(message, log_file):
    print(message)
    with open(log_file, 'a') as file:
        file.write(message + '\n')

HOST = '127.0.0.1'
PORT = 65432
LOG_FILE = '/data/openpilot/selfdrive/car/volkswagen/output.log'  # 你可以将这个路径修改为你希望的日志文件位置

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
            log_and_print(str(deserialized_data), LOG_FILE)
            # 清除缓冲区以便接收新的 JSON 数据
            data = ''
        except json.JSONDecodeError:
            # 如果反序列化失败，则打印原始数据
            log_and_print("Incomplete JSON: " + data, LOG_FILE)
