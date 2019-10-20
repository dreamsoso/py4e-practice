fhand = open('words.txt')
d = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
print(d)

while True:
    target = input("target to find in dict:")
    if target == 'WOOLALA': break
    if target in d: print("%s is in dict" % target)
    else: print("%s is not in dict" % target)
print("Process done")