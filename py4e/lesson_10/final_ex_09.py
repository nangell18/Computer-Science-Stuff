fname = input('enter file name: ')
if len(fname) < 1 : fname = r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_10\intro.txt'
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        # idiom: retrieve/create/update counter
        dic[word] = dic.get(word,0)+1
        # print(word, 'new', dic[word])

# print the dic
print(dic)

#now we want to gind the most common word
largest = -1
theWord = None
for key,value in dic.items():
    if value > largest:
        largest = value
        theWord = key #capture the key that was largest
print('The highest word is:\t',theWord, '\t',"with the value of:", largest)
