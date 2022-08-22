# strings
strHours = input("Enter Hours: ")
strRate = input("Enter rate: ")
# floats
flHours = float(strHours)
flRate = float(strRate)

if flHours > 40:
    # print("Overtime")
    reg = flRate * flHours
    otp = (flHours - 40.0) * (flRate * 0.5)
    # print(reg, otp)
    pay = reg + otp
else:
    # print("Regular")
    pay = flHours * flRate 
print("Pay:",pay)