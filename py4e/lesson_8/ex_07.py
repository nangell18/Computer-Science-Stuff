xfile = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\file.txt')
#print(xfile)
#print(xfile.read())

# just read the entire file
for cheese in xfile:
    print(cheese)

#you need to declare a different file name everytime you want to do something different to that file
xfile1 = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\file.txt')
count = 0
for line in xfile1:
    count = count +1
print('line count!!:',count, '\n\n')


xfile2 = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\file.txt')
for line in xfile2:
    line = line.rstrip() #get rid of the whitespace below
    if line.startswith('From:'):
        print(line)


xfile3 = open(r'C:\Users\student\Documents\GitHub\Computer-Science-Stuff\py4e\lesson_8\file.txt')
for line in xfile3:
    line = line.rstrip()
    if not '@uct.ac.za' in line: #if the string is not in line, then skip it and then print that line at the end
        continue
    print(line)



    # use quit() function to stop the entire program all together