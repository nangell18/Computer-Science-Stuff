fh = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\mbox-short.txt')

#read file
for lx in fh:
    ly = lx.rstrip() #delte all the '\n' 
    print(ly.upper())