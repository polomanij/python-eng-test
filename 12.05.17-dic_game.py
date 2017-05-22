import random

'''print("Welcome to the english test!!\n"
      "You will see the word on the russian language\n"
      "and then translate it on the next line.\n"
      "Good luck!\n")
'''
#--------------------------------------------------
def makeDic():
    file = open("some.txt")

    dic = {}
    line = file.readline()

    while line != '':
        lineArr = line.split(' ')
        dic[lineArr[0].rstrip()] = lineArr[1].rstrip()
        line = file.readline()
    file.close()
    return dic
#--------------------------------------------------

def writeWord():
    engWord = input('Enter English word: ').rstrip()
    rusWord = input('Enter Russian word: ').rstrip()
    line = engWord + ' ' + rusWord

    file = open("some.txt", "a")
    file.write('\n' + line)

#++++++++++++++++++++++++++++++++++++++++++++++++++
def victorine():
    dic = makeDic()
    for key in dic:
        print (key, dic[key])
    maxNumQues = len(dic)
    numQues = int(input('Enter number of questions(max:' +  str(maxNumQues) + '): '))
    
    if numQues > maxNumQues:
        numQues = len(dic)
        
    right_answer = 0

    for i in range(numQues):
        word1, word2 = random.choice(list(dic.items()))
        dic.pop(word1)
        print(word2)
        inp_word = input('Translate: ')
        if inp_word == word1:
            right_answer += 1
    print('Right answers: ' + str(right_answer) + '/' + str(numQues))
#++++++++++++++++++++++++++++++++++++++++++++++++++
