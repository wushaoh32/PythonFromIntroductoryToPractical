#处理数组、矩阵
#图像的灰度处理
import numpy as np
import matplotlib.pyplot as plt

n1 = plt.imread('google.jpg')
print(type(n1),n1)#三维数组 1、最高维表示图像的高，次高维表示图像的宽，最低维表示RGB
plt.imshow(n1)

#编写灰度的公式
n2 = np.array([0.299,0.587,0.144])#创建数组
#点乘运算
x = np.dot(n1,n2)
#传入数组，显示灰度
plt.imshow(x,cmap='gray')
#显示图像
plt.show()

