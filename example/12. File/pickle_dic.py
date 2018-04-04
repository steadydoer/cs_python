import pickle

f = open("dictionary.dat", "rb")
dic=pickle.load(f)
f.close()

for key in dic:
    print(key)

word = input("검색하려는 단어를 입력하시오. ")
while(word != "1"):
    if word in dic:
        print("%s의 뜻은 \'%s\'입니다." %(word, dic[word]))
        word = input("계속하려면 단어를 입력하시고 끝내려면 1을 입력하시오. ")
    else:
        word = input("사전에 없는 단어입니다. 다른 단어를 입력하시오. 끝내려면 1을 입력하시오. ")
