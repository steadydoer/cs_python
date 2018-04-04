import pickle

my_list = ["Yoon", "2010100", 95]
f = open('testPickle.dat', 'wb')
pickle.dump(my_list, f)
f.close()
