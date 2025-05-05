from multiprocessing import Process
import os,time
def test():
    print(f"我是子进程，我的pid是：{os.getpid()},我的父进程是：{os.getppid()}")
    time.sleep(1)
if __name__ == '__main__':
    print("主进程开始执行")
    lst=[]
    for i in range(5):
        #创建进程,其他参数可以不写，但是参数必须写，写的是函数的名字
        P = Process(target=test)
        #启动子进程
        P.start()
        #启动中的进程添加到列表中
        lst.append(P)
    #阻塞主进程
    for item in lst:
        item.join()
    print("主进程执行结束")