import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count=0
threshold = 3000
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    s = data.decode()
    print("count=%d len(s)=%d" %(count,len(s)))
    if (count+len(s)) <= threshold:
        if count == 0:
            output=s
            count=count+len(s)
        else:
            count+=len(s)
            output=output+s
    else:
        output=output+s[:(threshold-count)]
        count=threshold
        break
print(output)
mysock.close()
