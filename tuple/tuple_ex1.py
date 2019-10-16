fname = input("Enter file name:")
fhand = open(fname)
d = dict()
maxinum = None
for line in fhand:
    if line.startswith('From') and '@' in line:
        words = line.split()
        if len(words) > 1:
            if words[1] in d:
                d[words[1]]+=1
            else:
                d[words[1]]=1

tmp=d.items()
print(tmp)
l=list()
for key,value in tmp:
    l.append((key,value))
l.sort(reverse=True)
print(l[0])
print("l=",l)

