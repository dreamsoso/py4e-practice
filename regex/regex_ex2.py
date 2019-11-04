import re

fname = input('Enter file:')
fhand = open(fname)

count=0
total=0
for line in fhand:
    x = re.findall('^New .*: ([0-9]+)', line)
    if len(x)>0:
        count +=1
        total += int(x[0])
if count:
    print('average=%d' %(total/count))