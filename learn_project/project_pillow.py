#图像处理的第三方库、支持图像存储、处理和显示
#做一个图像颜色的交换
from PIL import Image
#加载到程序
im = Image.open('google.jpg')
#print(type(im),im)
#提取RGB图像的颜色，返回结果是图像的副本
r,g,b = im.split()
# print(r)
# print(g)
# print(b)
#合并通道
om = Image.merge('RGB',(r,b,g))
om.save('new_google.jpg')
