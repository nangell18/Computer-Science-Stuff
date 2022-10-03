# better way of adding values to a loop in lesson_9

#the benefit of using this though, is the fact that it is using less memory
# this is very important when it comes to adding up a billion numbers

num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    num = num + 1
    tot = tot + fval

print(tot,num,tot/num)