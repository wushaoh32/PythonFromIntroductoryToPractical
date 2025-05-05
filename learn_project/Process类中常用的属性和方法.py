from multiprocessing import Process
import os,time
#函数式创建子进程
def sub_process(name):
    print(f"子进程PID:{os.getpid()},父进程的PID{os.getppid()}--------{name}")

    time.sleep(1)
#子进程2
def sub_process2(name):
    print(f"子进程PID:{os.getpid()},父进程的PID{os.getppid()}--------{name}")

    time.sleep(1)
if __name__ == '__main__':
    print("主进程开始执行")
    #主进程
    for i in range(5):
        #只有一个参数，元组中也要有逗号，args位置参数
        p1 = Process(target=sub_process,args=('wsh',))
        #创建第二个子进程
        p2 = Process(target=sub_process2,args=(24,))
        p1.start()
        p2.start()
        print(p1.name,"是否执行完毕：",p1.is_alive())
        print(p2.name,"是否执行完毕：",p2.is_alive())
        print(p1.name,"PID是:",p1.pid)
        print(p2.name,"PID是:",p2.pid)
        #阻塞主进程
        p1.join()
        p2.join()
    print("父进程执行完毕")
