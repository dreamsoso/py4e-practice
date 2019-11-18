import socket
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=0
threshold = 3000
for line in fhand:
    s = line.decode()
    if (count+len(s)) <= threshold:
        if count == 0:
            output=s
            count=count+len(s)
        else:
            count+=len(s)
            output=output+s
    else:
        if count == 0:
            output=s[:(threshold-count)]
        else:
            output=output+s[:(threshold-count)]
        count=threshold
        break
print(output)
print("total character=",count)

