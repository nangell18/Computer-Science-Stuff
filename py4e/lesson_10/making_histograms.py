counts = dict()
names = ['nate', 'jake', 'nate', 'bob', 'jake']

#this is forbeginners
#for name in names:
    #if name not in counts:
        #counts[name] = 1
    #else:
        #counts[name] = counts[name] + 1

# this is using the get method
for name in names:
    counts[name] = counts.get(name, 0) + 1 #the zero is the default

print(counts)