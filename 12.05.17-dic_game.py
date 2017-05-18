import random

print("Welcome to the english test!!\n"
      "You will see the word on the russian language\n"
      "and then translate it on the next line.\n"
      "Good luck!\n")

file = open("some.txt")

#--------------------------------------------------
dic = {}
line1 = file.readline()
line2 = file.readline()

while line2 != '':
    dic[line1.rstrip()] = line2.rstrip()
    line1 = file.readline()
    line2 = file.readline()
file.close()
#--------------------------------------------------

#++++++++++++++++++++++++++++++++++++++++++++++++++
def victorine(num_of_quest):
    right_answer = 0
    used_words = []

    for i in range(num_of_quest):
        word1, word2 = random.choice(list(dic.items()))
        dic.pop(word1)
        print(word2)
        inp_word = input('Translate: ')
        if inp_word == word1[1 : len(word1) - 1]:
            right_answer += 1
    print('Right answers: ' + str(right_answer) + '/' + str(num_of_quest))
#++++++++++++++++++++++++++++++++++++++++++++++++++
