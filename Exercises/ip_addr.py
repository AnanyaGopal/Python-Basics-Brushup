'Learn to parse column-oriented text intented for humans to read'
# goal: show neatly formatted output.
# 51.51.51.51 loopback0
# 1.20.30.40  MgmtEth0/RSP0/CPU0/0
'''
The input file (ipv4_int_bri.txt) looks like this:
Interface                      IP-Address      Status                Protocol
Loopback0                      51.51.51.51     Up                    Up
MgmtEth0/RSP0/CPU0/0           1.20.30.40      Up                    Up
MgmtEth0/RSP0/CPU0/1           unassigned      Down                  Down
MgmtEth0/RSP1/CPU0/0           unassigned      Up                    Up
HundredGigE0/1/0/0             unassigned      Shutdown              Down
HundredGigE0/1/0/1             unassigned      Shutdown              Down
TenGigE0/2/0/0                 unassigned      Down                  Down
TenGigE0/2/0/1                 unassigned      Down                  Down
'''

'''
1st  Approach: Read line by line.
'''

# Open file.
# Read the first line --> That's the headline.
 # Interface  IP-Address Status Protocol
# Repeat the following steps in a loop until EOF.:
    # Read one entry
    # Looks like this: GigabitEthernet0/7/0/3 unassigned Down Down
    # Split this entry into a field.


processed_file = open('ipaddr_out.txt', 'w')
f = open('notes/ipv4_int_bri.txt')
header = next(f)
#print(header)

for line in f:
    entry = line.split()
    interface, ip_address, status, protocol = entry
    # print('%-15s %s') % (ipaddr, interface))
    if status.lower() == 'up':
        #print("%s %s %s" % (ip_address, ' '*(15-len(ip_address)), interface))
        processed_file.write("%s %s %s\n" % (ip_address, ' '*(15-len(ip_address)), interface))
    
f.close()
processed_file.close()


'''
2nd Approach: Acquire entire file.
'''

# Read entire file.
f = open('notes/ipv4_int_bri.txt')
output = f.read()

# [0: len(lines)-1 ] is equivalent to [0:-1] is equivalent to
# 0th to the last element.
lines = output.split('\n')[0:-1]

# Parse data and convert it into a convenient form.
ifaces = [] # ifaces is the list of tuples of all interfaces.
header = lines[0]


# [1: len(lines)] is equivalent to [1:] is equivalent to
# 1st to the last element. 
for line in lines[1:len(lines)]:
    fields = line.split()
    iface = tuple(fields)
    ifaces.append(iface)

# Analysis, testing, formatting and outputting.
print('%-15s %s' % ("IP address", "Interface"))
for iface in ifaces:
    interface, ipaddr, status, protocol = iface
    if status.lower() == 'up':
        print('%-15s %s' % (ipaddr, interface))

'''
2nd Approach is better than 1st:
    1. Clock performance:
    2. Team work. 
'''
