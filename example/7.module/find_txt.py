import os
import queue

def get_subdir(path): 
    try:
        dir_names=[]
        dirfiles = os.listdir(path)
        for each in dirfiles:
            full_name = path + each
            if os.path.isdir(full_name):
                dir_names.append(full_name+"/")
        return dir_names        
    except PermissionError:
        return

def find_txtfile(path):
    try:
        result = []
        dirfiles = os.listdir(path)
        for each in dirfiles:
            if ".txt" in each:
                result.append(path + each)
        return result
    except PermissionError:
        return
                

dir_queue = queue.Queue()
dir_queue.put("/home/user/")	# 검색하고자 하는 디렉터리를 줄 앞에 세움 

all_dirs = []
find_result= []
while not dir_queue.empty():	
    dir_name = dir_queue.get()
    find_files = find_txtfile(dir_name)
    if len(find_files) > 0:
        for i in find_files:
            find_result.append(i)
    subdir_names = get_subdir(dir_name)
    for each in subdir_names:
        dir_queue.put(each)

print(find_result)
