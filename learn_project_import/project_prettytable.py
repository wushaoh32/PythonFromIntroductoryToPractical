#实现仿高铁收票系统
import prettytable as pt
#显示坐席
def show_ticket(row_num):
    tb=pt.PrettyTable()
#设置标题（表格的排头部分）
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
