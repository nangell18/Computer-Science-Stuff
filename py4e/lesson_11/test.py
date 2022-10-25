fname = r'C:\Users\student\Desktop\blah.txt'
hand = open(fname)

query = []
for line in hand:
    sentences = line.split('\n')
    query.append(sentences)

print(query)

text = """

High‑frequ... trading

Arbitrage

Mean reversion

Time‑weig... average price

Trend following
See more
Feedback
trading algorithms software
high-frequency trading algorithm
algorithmic trading python
algorithmic trading strategies
forex trading algorithm
algorithmic trading course
best trading algorithms
is algo trading profitable"""

words = text.split('\n')

#print(words)