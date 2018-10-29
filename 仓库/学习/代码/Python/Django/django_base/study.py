import socket
from rest_framework import status

# 创建UDP套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # 创建目标地址
# address = ('192.168.138.255', 7878)
#
# # 设置socket允许发送广播消息
# udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
#
# # 设置需要发送的数据
# data = 'hello world'
#
# # 编码
# data = data.encode()
#
# # 发送数据
#
# udp_socket.sendto(data, address)
#
# # 接受数据
# recv_data, ip_port = udp_socket.recvfrom(1024)
# print(ip_port)
# # 解码
# recv_data = recv_data.decode('gbk')
#
# print(recv_data)
#
# # 关闭套接字
# udp_socket.close()

# # 创建TCP套接字
# tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接
# server_ip = '192.168.138.29'
# server_port = 7878
# tcp_client.connect((server_ip, server_port))
#
# # 设置数据
# data = 'hello'
#
# # 编码
# data = data.encode()
#
# # 发送数据
# tcp_client.send(data)
#
# # 接受数据
# recv_data = tcp_client.recv(1024)
#
#
# # 解码
# recv_data = recv_data.decode('gbk')
# print(recv_data)
#
# # 关闭连接
# tcp_client.close()


# # 创建TCP套接字
# tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 设置立即释放端口
# tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#
# # 绑定地址
# tcp_server.bind(('', 7878))
#
# # 设置监听
# tcp_server.listen(128)
#
# # 接受客户端请求
# tcp_client, ip_port = tcp_server.accept()
# print(ip_port)
#
# # 接受数据
# recv_data = tcp_client.recv(1024)
#
#
# # 解码
# recv_data = recv_data.decode('gbk')
# print(recv_data)
#
# # 设置数据
# data = 'hello'
#
# # 编码
# data = data.encode()
#
# # 发送数据
# tcp_client.send(data)
#
# # 关闭连接
# tcp_client.close()
# tcp_server.close()

import threading

# def sing(name, age):
#     print(name, age)
#     for i in range(10):
#         print('sing', i)
#         while True:
#             pass
#
# def dance():
#     for i in range(10):
#         print('dance', i)
#
#
# sub_thread1 = threading.Thread(target=sing, kwargs={'name': 'zhang', 'age':15})
# sub_thread2 = threading.Thread(target=dance, )
# sub_thread1.daemon = True
#
# sub_thread1.start()
# sub_thread2.start()

# class MyThread(threading.Thread):
#     """自定义线程"""
#
#     def __init__(self, info1, info2):
#
#         super(MyThread, self).__init__()
#         self.info1 = info1
#         self.info2 = info2
#
#
#     def test1(self):
#         print(self.info1)
#
#     def test2(self):
#         print(self.info2)
#
#     def run(self):
#         self.test1()
#         self.test2()
#
#
# if __name__ == '__main__':
#     my_thread = MyThread('测试1', '测试2')
#     my_thread.start()

# lock = threading.Lock()
#
# g_num = 0
#
# def sum_num1():
#     lock.acquire()
#     for i in range(1000000):
#         global g_num
#         g_num +=1
#     print('sum1:', g_num)
#     lock.release()
#
#
# def sum_num2():
#     lock.acquire()
#     for i in range(1000000):
#         global g_num
#         g_num +=1
#     print('sum2:', g_num)
#     lock.release()
#
# if __name__ == '__main__':
#     sub1 = threading.Thread(target=sum_num1)
#     sub2 = threading.Thread(target=sum_num2)
#     sub1.start()
#     sub2.start()
# def __init__(self, name):
#     self.name = name
#
# Hello = type('Student', (object, ), {'__init__': __init__, 'hello': lambda self, e: print(self.name)})
# hello = Hello('张三')
#
# hello.hello('p')

class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # print(super())
        return super().__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    __metaclass__ = ListMetaclass

l = MyList()
print(MyList.__mro__)
l.add(1)
print(l)