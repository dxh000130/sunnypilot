# socket_manager.py
import select
import socket
import json

class SocketManager:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 65432

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setblocking(False)  # 设置为非阻塞模式
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()

        self.conn = None
        self.addr = None

    def check_for_connection(self):
        if self.conn == None:
            readable, _, _ = select.select([self.s], [], [], 0)  # 轮询，0秒超时
            if readable:  # 如果socket可读，意味着有客户端尝试连接
                self.conn, self.addr = self.s.accept()

    def send_data(self, data):
        if self.conn != None:
            if self.conn:
                serialized_data = json.dumps(data)
                try:
                    self.conn.sendall(serialized_data.encode('utf-8'))
                except BrokenPipeError:
                    self.conn.close()
                    self.conn = None

socket_manager_instance = SocketManager()  # 创建SocketManager的实例
