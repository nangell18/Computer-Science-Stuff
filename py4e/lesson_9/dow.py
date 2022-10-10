fh = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\mbox-short.txt')

#read file
for line in fh:
    line = line.rstrip() #delte all the '\n' 
    #print("Line:",line) # debug
    words = line.split()
    #print("Words:",words) #debug

    #the code, len(words)... is our gaurdian
    if len(words) < 3: #reason for this is because we only use words that are greater than but not inclduing 3. all the days have three letters
        continue
    if words[0] != 'From' :
        #print('ignore') #debug 
        continue
    print(words[2])


    # we can also do this, compound gaurdian
    if len(words) < 3 or words[0] != 'From' : #the gaurdian has to come first though
        #print('ignore') #debug 
        continue
    print(words[2])