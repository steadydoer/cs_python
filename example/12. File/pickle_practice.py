import pickle

f = open("myDic.dat", "wb")
pickle.dump({"waiver": "권리포기, 면제", "tuition":"수업료", "insurance":"보험"}, f)
f.close()

f = open("myDic.dat", "rb")
dic = pickle.load(f)
print(dic)
f.close
