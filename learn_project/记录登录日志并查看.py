import time
def show_info():
    print('输入提示数字，执行相应的操作：0.退出 1.查看登录日志')

#记录日志
def write_log_info(username):
    with open('log.txt','a',encoding = 'utf-8') as file:
        # time.time时间戳（返回的是从1970开始的一个毫秒值）；strftime是将时间对象格式化为指定的字符串格式;%a是星期几的缩写
        s = f'用户名{username},登录时间：{time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')
#读取日志
def read_log_info():
    with open('log.txt','r',encoding = 'utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line)

if __name__ == '__main__':
    #write_log_info('admin')
    username = input('请输入用户名：')
    pwd = input('请输入密码：')
    if username == 'admin' and pwd == 'admin':
        print('登录成功')
        #将登录信息写入日志文件
        write_log_info(username)
        #提示用户操作
        show_info()
        num = int(input('请输入要操作的数字'))
        while True:
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                print('查看登录日志：')
                read_log_info()
                show_info()#再调一次显示信息
                break
            else:
                print('输入的数字有误')
                show_info()
    else:
        print('用户名和密码不正确')
