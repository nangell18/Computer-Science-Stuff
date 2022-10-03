from operator import le

#this uses more memory though. it is easier to code but not good for the amount of memory it uses
numList = list()

while True:
    inp = input("enter a number: ")
    if inp == 'done' : break
    value = float(inp)
    numList.append(value)

average = sum(numList) / len(numList)
print("The average is: ",average)