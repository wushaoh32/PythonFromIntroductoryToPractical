import pdfplumber
#打开PDF文件
with pdfplumber.open('数据库面试资源库.pdf') as pdf:#这个文件要放到外层的文件夹下
    for i in pdf.pages:
        print(i.extract_text())
        print(f'---------第{i.page_number}页结束')
        