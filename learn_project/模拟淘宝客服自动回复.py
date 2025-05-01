def find_answer(question):

    with open('replay.txt','r',encoding = 'utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            keyword = line.split('|')[0]
            reply =  line.split('|')[1]
            if keyword in question:
                return  reply
        return False
if __name__ == '__main__':
    question = input('请讲：')
    while True:
        if question == 'bye':
            break
        else:
            replay = find_answer(question)
            if replay==False:
                question = input('不知道你说的什么')
            else:
                print(replay)
                question = input('再问问？')