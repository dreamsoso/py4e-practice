fname = input("Enter file name:")
fhand = open(fname)
d = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 1:
            if words[1] in d:
                d[words[1]]+=1
            else:
                d[words[1]]=1
print(d)
