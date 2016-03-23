__auther__ = 'Victor'

import select
import socket
import sys
import queue

# 创建一个TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
# 绑定socket到指定端口
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)
# 监听连接的地址
server.listen(5)
inputs = [server]
# Socket的读操作
outputs = []
# socket的写操作
message_queues = {}
while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print( '\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # 监听句柄序列，如果某个发生变化，select的第一个rLest会拿到数据，output只要有数据wLest就能获取到，select的第三个参数inputs用来监测异常，并赋值给exceptional。
    # 监听inputs，outputs，inputs  如果他们的值有变化，就将分别赋值给readable，writable，exceptional。
    for s in readable:
        # 遍历readable的值。
        if s is server:
            connection, client_address = s.accept()
            # 如果s 是server，那么server socket将接收连接。
            print('new connection from', client_address)
            # 打印出连接客户端的地址。
            connection.setblocking(False)
            # 设置socket 为非阻塞模式。
            inputs.append(connection)
            # 因为有读操作发生，所以将此连接加入inputs
            message_queues[connection] = queue.Queue()
            # 为每个连接创建一个queue队列。使得每个连接接收到正确的数据。
        else:
            data = s.recv(1024)
            # 如果s不是server，说明客户端连接来了，那么就接受客户端的数据。
            if data:
                # 如果接收到客户端的数据
                print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()) )
                message_queues[s].put(data)
                # 将收到的数据放入队列中
                if s not in outputs:
                    outputs.append(s)
                    # 将socket客户端的连接加入select的output中，并且用来返回给客户端数据。
            else:
                print('closing', client_address, 'after reading no data')
                # 如果没有收到客户端发来的空消息，则说明客户端已经断开连接。
                if s in outputs:
                    outputs.remove(s)
                    # 既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                inputs.remove(s)
                # inputs中也删除掉
                s.close()
                # 把这个连接关闭掉
                del message_queues[s]
                # 删除此客户端的消息队列

    for s in writable:
        # 遍历output的数据
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # 获取对应客户端消息队列中的数据，如果队列中的数据为空，从消息队列中移除此客户端连接。
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print( 'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
            # 如果消息队列有数据，则发送给客户端。
    for s in exceptional:
        # 处理 "exceptional conditions"
        print('handling exceptional condition for', s.getpeername() )
        inputs.remove(s)
        # 取消对出现异常的客户端的监听
        if s in outputs:
            outputs.remove(s)
            # 移除客户端的连接对象。
        s.close()
        # 关闭此socket连接
        del message_queues[s]
        # 删除此消息队列。

'''

在select/poll时代，服务器进程每次都把这100万个连接告诉操作系统(从用户态复制句柄数据结构到内核态)，让操作系统内核去查询这些套接字上是否有事件发生，

轮询完后，再将句柄数据复制到用户态，让服务器应用程序轮询处理已发生的网络事件，这一过程资源消耗较大，因此，select/poll一般只能处理几千的并发连接。

epoll的设计和实现与select完全不同。epoll通过在Linux内核中申请一个简易的文件系统(文件系统一般用什么数据结构实现？B+树)。把原先的select/poll调用分成了3个部分：

1）调用epoll_create()建立一个epoll对象(在epoll文件系统中为这个句柄对象分配资源)

2）调用epoll_ctl向epoll对象中添加这100万个连接的套接字

3）调用epoll_wait收集发生的事件的连接

'''


