def computePay(hours,rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate 
    print("returning", pay)
    return pay

# strings
strHours = input("Enter Hours: ")
strRate = input("Enter rate: ")
# floats
flHours = float(strHours)
flRate = float(strRate)

pay = computePay(flHours, flRate)

print("Pay:",pay)