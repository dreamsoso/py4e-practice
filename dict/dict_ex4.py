fname = input("Enter file name:")
fhand = open(fname)
d = dict()
maxinum = None
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 1:
            if words[1] in d:
                d[words[1]]+=1
            else:
                d[words[1]]=1
for key in d:
    if maxinum is None or d[key] > maxinum:
        maxinum = d[key]
        owner = key

print(d)
print(list(d.values()))
print("key=%s max=%d" % (owner, maxinum))
