fname = input("Enter file name:")
fhand = open(fname)
d = dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        if len(words) > 2:
            if words[2] in d:
                d[words[2]]+=1
            else:
                d[words[2]]=1
print(d)
