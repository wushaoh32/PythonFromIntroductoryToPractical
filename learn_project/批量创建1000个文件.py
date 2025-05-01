import random
import os
import os.path

def create_filename():
    """这个函数把名字都创建好"""
    filename_lst = []#创建一个空列表，收集生成的文件名
    # 物资类别
    lst = ['水果','烟酒','粮油','肉蛋','蔬菜']
    code = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(1,1001):
        filename = ''#准备拼接文件名
        if i <10:
            filename += '000' + str(i)
        elif i <100:
            filename += '00' + str(i)
        elif i <1000:
            filename += '0' + str(i)
        else:
            filename += str(i)
        #拼接类别
        filename += '_' + random.choice(lst)
        #拼接识别码
        s = ''
        for j in range(9):
            s += random.choice(code)
        filename += '_' + s
        filename_lst.append(filename)
    return filename_lst


def create_file(filename):
    with open(filename, 'w') as file :
        pass


if __name__ == '__main__':
    #print(create_filename())
    #开始在指定路径下创建文件
    path='./1000file'
    if not os.path.exists(path):
        os.makedirs(path)
    LST = create_filename()#调用获取文件名
    for item in LST:
        create_file(os.path.join(path, item)+'.txt')