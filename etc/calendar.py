Month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# key:value , key:value pair
day = 1
for i in range(1,13):
    print("{}월".format(i))
    start = day % 7
    print("\t"*start, end="")
    for j in range(Month[i]): # 310
        if(day % 7 == 6):
            print("{}".format(j+1))
        else:
            print("{}\t".format(j+1), end="")
        day += 1
    print()
    print()
# space = "{:<5}"
# for i in range(1,13):
#     print("{}월".format(i))
#     start = day % 7
#     for k in range(start):
#         print(space.format(" "), end="")
#     for j in range(Month[i]):
#         if(day % 7 == 6):
#             print(space.format(j+1))
#         else:
#             print(space.format(j+1), end="")
#         day += 1
#     print()
#     print()
