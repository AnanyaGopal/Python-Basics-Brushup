'''
    Acquire stock information and convert it to a convenient format.
    [('CSCO',100,18.04), (ANTN, 200, 45.03), ... ]

    
'''
'''
   stocks.txt has:

CSCO,100,18.04
ANTM,200,45.03
CSCO,150,19.05
MSFT,250,80.56
IBM,500,22.01
ANTM,250,44.23
GOOG,200,501.45
CSCO,175,19.56
MSFT,75,80.81
GOOG,300,502.65
IBM,150,25.01
   
'''

f = open('notes/stocks.txt')
stock_list = []
for line in f:
    stock = line.rstrip().split(',')
    # Unpacking
    name, num, price = stock 
    trade = (name, int(num), float(price))
    stock_list.append(trade)

print(stock_list)
f.close()

