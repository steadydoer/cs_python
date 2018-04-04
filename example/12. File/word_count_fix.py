f = open("Les_Miserables-Victor_Hugo.txt", "r")
word_list = f.read().split() #파일을 읽고 공백을 기준으로 나눈 문자열들을 리스트로 저장
word_list.sort()#리스트 정렬
wordCount={}#단어들의 횟수를 저장하기 위한 사전 정의


#단어 구분에 필요 없는 문장부호를 제거 한 후 위에 정의된 사전에 문자열을 키로 횟수를 값으로 하여 저장
for i in range(len(word_list)):
    word_list[i] = word_list[i].replace(".","").replace(",","").replace("?","").replace("!","").replace("\'","").replace("\"","")
    word_list[i] = word_list[i].upper()
    if  not word_list[i] in wordCount:
        wordCount[word_list[i]] = 1
    else:
        wordCount[word_list[i]] += 1


values = wordCount.values()#wordCount 사전의 값들로 구성된 리스트 만들기
n = 0
for val in values:#values라는 리스트를 이용하여 단어들의 총 나타난 횟수를 저장
    n += val


wordCountList = []#빈도수를 비교하기 위한 리스트 정의
for i in range(len(wordCount)):#사전의 키와 값을 정렬 가능한 리스트로 만듦
    wordCountList.append(wordCount.popitem())

wordCountList.sort(key= lambda x : x[1] , reverse=True)#람다 함수 이용 단어의 횟수를 기준으로 정렬, 역순정렬, 가장 많은 횟수가 제일 처음
print(wordCountList)
print("%s is 1st word and percentage is %f%%." %(wordCountList[0][0], (wordCountList[0][1]/n)*100))
print("%s is 2nd word and percentage is %f%%." %(wordCountList[1][0], (wordCountList[1][1]/n)*100))
print("%s is 3rd word and percentage is %f%%." %(wordCountList[2][0], (wordCountList[2][1]/n)*100))
print("%s is 4th word and percentage is %f%%." %(wordCountList[3][0], (wordCountList[3][1]/n)*100))
