fname = input('enter file name: ')
if len(fname) < 1 : fname = r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_10\intro.txt'
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        # print(word) print the word
        if word in dic :
            dic[word] = dic[word] + 1
            # print('**exsiting**') see if it is exsisting
        else:
            dic[word] = 1
            #print('**NEW**') print if it is new
        print(word, dic[word])

# print the dic
print(dic)