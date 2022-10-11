fname = input('enter file name: ')
if len(fname) < 1 : fname = r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_10\intro.txt'
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        oldCount = dic.get(word,0)
        print(word,'old',oldCount)
        newCount = oldCount + 1
        dic[word] = newCount
        print(word,'new',newCount)

# print the dic
print(dic)