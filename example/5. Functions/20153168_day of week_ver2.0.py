# 요일 구하기를 위해 설정된 변수 n의 값 초기화
n = 0

# 평년과 윤년의 달을 키로 날수를 값으로 하는 사전 만들기
Month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
LeapMonth = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#년도를 입력 받는다.
print ("기준년을 입력하십시오. \n기준년 : ", end='')
year = int(input())

#년도가 1 이상의 정수만 입력받도록 한다.
while(year < 1):
    print ("입력한 기준년를 확인하십시오. 기준년는 1 이상의 정수만 입력할 수 있습니다.")
    print ("기준년을 입력하십시오. \n년도 : ", end='')
    year = int(input())
    
#월을 입력 받는다.
print ("기준월을 입력하십시오. \n기준월 : ", end='')
month = int(input())

#월이 1이상 12이하의 정수만 입력받도록 한다.
while(month < 1 or month > 12):
    print ("입력한 기준월을 확인하십시오. 기준월은 1과 12사이의 정수만 입력할 수 있습니다.")
    print ("기준월을 입력하십시오. \n기준월 : ", end='')
    month = int(input())

#일을 입력 받는다.
print ("기준일을 입력하십시오. \n기준일 : ", end='')
day = int(input())

#입력 받은 월에 따라 입력 받은 일의 범위를 제한한다.
if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    while (day < 1 or day > LeapMonth[month]):
        print("해당 월은 1일부터 %d일까지 있습니다." %LeapMonth[month])
        print("기준일을 입력하십시오. \n기준일 : ", end='')
        day = int(input())
else:
    while (day < 1 or day > Month[month]):
        print("해당 월은 1일부터 %d일까지 있습니다." %Month[month])
        print("일을 입력하십시오. \n기준일 : ", end='')
        day = int(input())

#며칠 후를 입력 받는다.
print("며칠 후의 날을 알고 싶습니까? 만약 음수를 입력한다면 며칠 전의 날을 구합니다.", end=' ') 
deltaday = int(input())

#for문을 이용하여 윤년은 366일을 평년은 365일을 더한다. [1, 2, ..., year-1]
for i in range(1, year):
    if i%400 == 0 or ( i%4 == 0 and i%100 != 0):
        n += 366
    else:
        n += 365
   
#for문을 이용하여 입력받은 월의 전월까지의 일수를 더한다. [1, 2, ..., month-1]
if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    for i in range(1, month):
        n += LeapMonth[i]
else:
    for i in range(1, month):
        n += Month[i]

#입력받은 일수를 더한다.
n += day

#날의 변화랑을 더한다.
p = n + deltaday
while( p < 1):
    print("1년 1월 1일 전의 연원일과 요일은 구할 수 없습니다. 다시 입력해주세요.", end=' ')
    deltaday = int(input())
    p = n + deltaday

n += deltaday 

#7로 나누어 나머지를 구해놓는다.
remainder = n%7

#변수초기화
year = 1
month = 1
day = 0

#n을 이용하여 년월일 구하기
while(n > 365):
    if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
        if n == 366:
            break
        else:
            n -= 366
            year += 1
    else:
        n -= 365
        year += 1

if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    while(n > LeapMonth[month]):
        n -= LeapMonth[month]
        month += 1
else:
    while(n > Month[month]):
        n -= Month[month]
        month += 1

day = n

#나머지에 따라 요일을 결정해서 출력한다.
dayofweek = ['일', '월', '화', '수', '목', '금', '토']
print("%d년 %d월 %d일은 %s요일입니다."%(year, month, day, dayofweek[remainder]))
