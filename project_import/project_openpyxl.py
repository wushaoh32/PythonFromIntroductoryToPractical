import openpyxl
import weather
html = weather.get_html()#发请求
lst = weather.parse_html(html)#解析数据
#创建一个excel工作簿
workbook = openpyxl.Workbook()#创建对象
#在Excel中创建工作表
sheet = workbook.create_sheet("景区天气")
#像工作表中添加数据
for item in lst:
    sheet.append(item)

workbook.save('景区天气.xlsx')