from sys import exit

fname = input('Enter file name:')

try:
    fp = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    print("File cannot be opened:",fname)
    exit()

count =0
for line in fp:
    count+=1
print("There were %d subject lines in %s\n" % (count, fname))
