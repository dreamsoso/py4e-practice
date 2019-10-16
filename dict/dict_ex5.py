fname = input("Enter file name:")
fhand = open(fname)
d = dict()
for line in fhand:
    if '@' in line and line.startswith('From'):
        words = line.split()
        if len(words) > 1:
            target = words[1]
            index = target.find('@')+1
            if target[index:] in d:
                d[target[index:]]+=1
            else:
                d[target[index:]]=1
print(d)

