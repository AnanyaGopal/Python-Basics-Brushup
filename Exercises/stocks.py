'''
    Acquire stock information and convert it to a convenient format.
    [('CSCO',100,18.04), (ANTN, 200, 45.03), ... ]


'''

f = open('notes/stocks.txt')
stock_list = []
for line in f:
    stock = line.rstrip().split(',')
    name, num, price = stock
    t = tuple(stock)
    stock_list.append(t)

print(stock_list)
f.close()

