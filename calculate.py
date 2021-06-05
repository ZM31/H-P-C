import socket
import  struct


class sever(object):

    def __init__(self,IP,port):
        self.IP = IP
        self.port = port         #计算节点init化

    def creatfp(self,filename,sock):
        # 接受所传输的文件
        # filename  文件名


        file_info_sie = struct.calcsize('128sl')
        # 接受文件名与文件大小信息
        buf = sock.recv(file_info_sie)
        # 判断是否接收到文件大小信息
        if buf:
            fileName, f_size = struct.unpack('128sl', buf)
            # 接受文件

            fp = open(filename, 'wb')
            has_re = 0
            while has_re != f_size:      # 根据所接受字节判断接受1024字节还是非空的真实字节数
                if f_size - has_re >= 1024:
                    data = sock.recv(1024)
                    data1 = data.decode('utf-8')
                    fp.write(data)
                    has_re += len(data1)
                else:
                    data = sock.recv(f_size - has_re)
                    data1 = data.decode('utf-8')
                    fp.write(data)
                    has_re += len(data1)

            fp.close()

    def creat(self):
        #计算节点启动
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.IP, self.port))
        s.listen(5)
        print('listen at port :', self.port)


        # 接受连接:
        sock, addr = s.accept()
        print('-----------------------------')
        print('connected by', addr)

        sock.send(b'Welcome!')  # 1.发送 Welcome 信息

        data = sock.recv(1024).decode('utf-8')
        fname = sock.recv(1024).decode('utf-8')
        print('The role and task is '+data)  # 2.接受Role 和 Task i信息

        a, c = data.split(' and ')



        # 3. 发送 ：该计算节点已接受Role 和 Task信息
        sock.send(('OK,Thread %s is received' % str(a)).encode('utf-8'))



        # 根据Task[i]选择执行策略
        if c == 'task1':
            data = sock.recv(1024).decode('utf-8')
            print(data)             # 3.1 接受数据文件信息
            # print('The task1  fname is ' + name +' and size is '+f_size )  # 3.1.receive  task1 information

            self.creatfp(data,sock)# 3.2 接受数据文件
            # data = sock.recv(1024)
            # print(data)
            self.creatfp('task1.py',sock)# 3.3 接受执行文件
            # print(data)
            # print('The task1 fname  is ' + name + ' and size is ' + f1_size)
            sock.send(('Thread %s local max is caculated...' % str(a)).encode('utf-8'))
            import task1     #导入刚刚接受的执行文件

            max = task1.max_value(fname, a) # 调用task1的方法计算所求值

            sock.send(('%s' % str(max)).encode('utf-8'))  # 4.发送局部最大值.
            print('Local max value is '+ str(max))

        if c == 'task2':
            num = sock.recv(1024).decode('utf-8')
            print(num)  # 3.1 接受 num值

            # data = sock.recv(1024).decode('utf-8')
            # print(data)
            self.creatfp('task2.py', sock)  # 3.2 接受执行文件

            sock.send(('Thread %s local zhihsu sum is caculated...' % str(a)).encode('utf-8'))


            import task2   #导入刚刚接受的执行文件

            sum = task2.summ(a,num) #调用task2的方法计算 所求值

            sock.send(('%s' % str(sum)).encode('utf-8'))  # 4.发送局部 sum
            print('Local sum is ' + str(sum))
        if c == 'task3':
            data = sock.recv(1024).decode('utf-8')
            print(data)  # 3.1 接受数据文件信息

            self.creatfp(data, sock)  # 3.2 接受数据文件
            self.creatfp('task3.py', sock)  # 3.3 接受执行文件
            sock.send(('Thread %s local max is caculated...' % str(a)).encode('utf-8'))

            import task3

            maxlist = task3.max_value(fname, a)
            sock.send(('%s' % str(maxlist[0])).encode('utf-8'))  # 4.发送局部最大值.
            print('Local sum is ' + str(maxlist[0]))

            data = sock.recv(1024).decode('utf-8')
            print(data)
            data = int(sock.recv(1024).decode('utf-8'))
            print(data)          #5.接收全局最大值以计算互质次大值

            sock.send(('Thread %s local maxzhihsu is caculated...' % str(a)).encode('utf-8'))

            maxzhi = task3.maxzhishu(maxlist,data)
            sock.send(('%s' % str(maxzhi)).encode('utf-8'))
            print('Local max zhishu is '+str(maxzhi))    # 6.发送局部互质次大值.


        sock.close
        print('Connection from %s:%s closed.' % addr)
        print('-----------------------------')


if __name__=='__main__':
    a=eval(input("Please input start way(1 、2 or 3):"))
    if a==1:
        sev=sever('192.168.186.1',5001)
        sev.creat()
    if a==2:
        sev=sever('192.168.186.1',5002)
        sev.creat()
    if a==3:
        sev=sever('192.168.158.65',5003)
        sev.creat()
