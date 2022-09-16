str = 'X-DSPAM-Confidence: 0.8475'
print(str)

# notice the many print statements that you use. this is all about debugging
ipos = str.find(':')
print(ipos)
piece = str[ipos+1:]
print(piece)
value = float(piece)
print(value)
