import requests
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

resp = requests.get(url)

#保存到本地
#wb:二进制写到本地,适用于像图片这种二进制文件的写入操作
#with是作用结束后释放资源；
#as file ：这部分是将open函数打开文件后返回的文件对象赋值给变量file，
#as是一个关键字，也就是将文件对象赋值给一个变量
with open('logo.png','wb') as file:
    file.write(resp.content)