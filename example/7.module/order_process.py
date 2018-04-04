#import subprocess

# 명령어창 실행 (Windows 운영체제)
#subprocess.call("firefox")

"""
import webbrowser 


# 웹 주소 설정
url = 'http://cyber2010.kookmin.ac.kr' 


# 기본 웹브라우저 구동
webbrowser.open(url)
"""
"""
import os

path = "./"
dirfiles = os.listdir(path)
print(dirfiles)
"""
"""
import os

path = "/home/user/"
dirfiles = os.listdir(path)
dir_names = []
file_names = []

for each in dirfiles:    
    full_name = path + each
    if os.path.isdir(full_name):
        dir_names.append(full_name + "/")    
    else:        
        file_names.append(full_name)

print("dir names: ")
print(dir_names)
print("file names: ")
print(file_names)
"""

import os
import queue


def get_subdir(path):	
	# 검색이 허가되지 않은 디렉토리 접근에 관한 예외처리 
	# (이후 예외처리 쳅터에서 자세히 다룸) 
	try:		
		dirfiles = os.listdir(path)
	except PermissionError:
		return
dir_queue = queue.Queue()
dir_queue.put("/home/user/")	# 검색하고자 하는 디렉터리를 줄 앞에 세움 

all_dirs = []
while not dir_queue.empty():	
	dir_name = dir_queue.get()
	all_dirs.append(dir_name)

	subdir_names = get_subdir(dir_name)
	for each in subdir_names:
		dir_queue.put(each)

print(all_dirs)
