#print ("Type 3 to continue, anything else to quit.")
#someInput = input()
#while someInput == '3' :
#    print ("Thank you fo the 3. Very kind of you.")
#    print ("Type 3 to continue, anything else to quit.")
#    someInput = input()
#print ("That's not 3, so I'm quitting now.")

#for i in range (1, 6):

#    print ()
#    print ('i =', i, end=' ')
#    print ('Hello, how', end=' ')
#    if i == 4:
#        break
#    print ('r u?')
#else: print('the end') #if i == 6, else execute


print ("Type big number first, then small one")
print ("a=", end=" ")
a = int(input())
print ("b=", end=" ")
b = int(input())

while(b): # b == 0 : false, b != 0 : true / false : exit , true : loop)
    #x = a
    #a = b
    #b = x%b
    a, b = b, a%b
print("GCD is %d" %a)
