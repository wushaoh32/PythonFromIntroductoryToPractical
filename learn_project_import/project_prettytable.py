#实现仿高铁收票系统
import prettytable as pt
from numpy.ma.core import choose


#显示坐席
def show_ticket(row_num):
    tb=pt.PrettyTable()
#设置标题（表格的排头部分）
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    #遍历有票
    for i in range(1,row_num+1):
        lst = [f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

#订票
def order_ticket(row_num,row,column):
    tb = pt.PrettyTable() #创建一张表格
    tb.fild_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        lst[int(column)] = '已售'
        tb.add_row(lst)
    else:
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)
if __name__ == '__main__':
    row_num = 6
    show_ticket(6)

    show_ticket(row_num)

    #开始售票
    choose_num = input('请输入你选择的坐席：如4,3表示第4排第3列：')
    row, column = choose_num.split(',')#系列解包赋值
    order_ticket(row_num,row,column)