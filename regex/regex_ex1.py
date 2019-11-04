import re

pattern = input("Enter a regular expression:")
fhand = open('mbox.txt')

count=0
for line in fhand:
    if re.search(pattern, line):
        count +=1

print("mbox.txt had %d lines that matched %s" %(count,pattern))