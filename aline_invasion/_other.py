# R = eval(input("请输入圆的半径："))
# perimeter =  2 * 3.14 * R
# area = 3.14 * R ** 2
# print("圆的周长：",perimeter,"圆的面积：",area)

# a,b,c,d = 'room'
# print(a)
# print(b)
# print(c)
# print(d)

# print('-'*100)

#name  = input("请输入您的姓名")

#age  = eval(input("请输入您的年龄："))

# n = 98

# if not n%2:
#     print(n,"n是偶数")
# print("----------------100到999之间的水仙花数---------------")
# for i in range(100,1000):
#     units_digit = i%10
#     tens_digits = (i//10)%10
#     hundreds_digits = i//100
#     #判断
#     if units_digit ** 3 + tens_digits ** 3+ hundreds_digits ** 3 == i :
#         print("水仙花数字：",i)

# print("----------------while计算累加和---------------")
# s,i = 0,1
# while i<=100:
#     s += i
#     i += 1
# else:
#     print("前100项的累和值是:",s,"此处的i的值是:",i)

print("----------------嵌套循环输出打印长方形和三角形---------------")

# for i in range(3):
#     for j in range(4):
#         print("*",end='')#print()是默认换行的
#     print()#里面自带一个默认换行，如果再往里面加\n，就相当于欢乐谷两行
print("----------------嵌套循环输出打印直角三角形---------------")
for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print()
print("----------------嵌套循环输出打印倒直角三角形---------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*",end='')
    print()
print("----------------嵌套循环输出打印等腰三角形---------------")
for i in range(1,6):
    #两部分：一部分打倒三角形，一部分打三角形
    #倒三角形
    for j in range(1,6-i):
        print(" ",end='')
    #等腰三角形:需要输出1，3，5，7，9  对行1,2,3,4,5
    for k in range(1,i*2):
        print("*",end='')
    print()
print("----------------嵌套循环输出打印棱形---------------")
row = eval(input("请输入棱形的行数："))
while row % 2 == 0 :
    print("请重新输入棱形行数：")
    row = eval(input("请输入棱形的行数："))
    
else: #当while循环正常结束时，执行eles的语法
    top_row = (row+1)//2
    for i in range(1,top_row+1):
        #两部分：一部分打倒三角形，一部分打三角形
        #倒三角形
        for j in range(1,top_row+1-i):
            print(" ",end='')
        #等腰三角形:需要输出1，3，5，7，9  对行1,2,3,4,5
        for k in range(1,i*2):
            print("*",end='')
        print()
    #棱形的下半部分
    bottom_row = row//2
    for l in range(1,bottom_row+1):
        #直角三角形
        for p in range(1,l+1):
            print(" ",end='')
        #下部分的等腰三角形
        for u in range(1,2*bottom_row-2*l+2):
            print("*",end='')
        print()