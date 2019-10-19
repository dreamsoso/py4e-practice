fname = input("Enter a file name:")

try:
    fhand = open(fname)
except:
    print("%s is not exists!\n" % fname)
count=0
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split();
        count+=1
        if len(words) > 2:
            print(words[1])

print("There were %d lines in the file with From as the first word" % count)