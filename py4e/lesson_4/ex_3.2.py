# strings
strHours = input("Enter Hours: ")
strRate = input("Enter rate: ")
# floats
try:
    flHours = float(strHours)
    flRate = float(strRate)
except:
    print("Error, please enter numeric input")
    quit()

print(flHours,flRate)
if flHours > 40:
    reg = flRate * flHours
    otp = (flHours - 40.0) * (flRate * 0.5)
    pay = reg + otp
else:
    pay = flHours * flRate 
print("Pay:",pay)