f = open("vocabulary.txt", "r")
word_list = f.read().split()
dic = {}


k = 1
mean = ""
for i in word_list:
    i = i.replace(".","").replace(",","").replace("?","").replace("!","").replace("\'","").replace("\"","")
    if i.isdecimal() == False:
        if k == 1:
            word = i
            k += 1
        elif k == 2:
            mean = mean + i
            k += 1
        else :
            mean = mean + ", " + i
    elif i.isdecimal() == True and k >= 2:
        k = 1
        dic[word] = mean
        mean = ""


word = input("검색하려는 단어를 입력하시오. ")
while(word != "1"):
    if word in dic:
        print("%s의 뜻은 \'%s\'입니다." %(word, dic[word]))
        word = input("계속하려면 단어를 입력하시고 끝내려면 1을 입력하시오. ")
    else:
        word = input("사전에 없는 단어입니다. 다른 단어를 입력하시오. 끝내려면 1을 입력하시오. ")

