def find_answer():
    with open('replay.txt','r',encoding = 'gbk') as file:
        while True:
            line = file.writeline()
            if line == '':
