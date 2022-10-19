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

tmp = list()
for k,v in dic.items():
    newTuple = (v,k)
    tmp.append(newTuple)

tmp = sorted(tmp, reverse=True)

#print(tmp[:5])

for v,k in tmp[:5]:
    print(v,k)
