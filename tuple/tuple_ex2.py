fname = input("Enter file name:")
fhand = open(fname)
d = dict()
maxinum = None
for line in fhand:
    if line.startswith('From') and '@' in line:
        words = line.split()
        if len(words) > 6:
            time = words[5].split(':')
            if time[0] in d:
                d[time[0]]+=1
            else:
                d[time[0]]=1

l=list(d.items())
l.sort()
print(l)
for hour,count in l:
    print(hour, count)

