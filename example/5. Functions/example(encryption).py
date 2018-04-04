print("Type sentence.")

st = input()

print("Type Key.", end=' ')

key = int(input())
key %= 26

List= []


for i in range(len(st)):
    if ('A' <= st[i] <= 'Z'):
        List.append(ord(st[i]) + key)
        if List[i] > ord('Z'):
            List[i] -= 26
    elif('a' <= st[i] <= 'z'):
        List.append(ord(st[i]) + key)
        if List[i] > ord('z'):
            List[i] -= 26
    else :
        List.append(ord(st[i]))


print("Encryption sentence : ", end='')
for i in range(len(List)):
    print(chr(List[i]), end='')

print()
print("Type decode key.", end=' ')

decryption_key = int(input())
decryption_key %= 26

dList = []

for i in range(len(List)):
    if ('A' <= chr(List[i]) <= 'Z'):
        dList.append(List[i] - key)
        if dList[i] < ord('a'):
            dList[i] += 26
    elif('a' <= chr(List[i]) <= 'z'):
        dList.append(List[i] - key)
        if dList[i] < ord('a'):
            dList[i] += 26
    else :
        dList.append(List[i])

print("Original sentence : ", end='')
for i in range(len(dList)):
    print(chr(dList[i]), end='')
