fhand = open('romeo.txt')
t = list()
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    for word in words:
	    if word in t: 
	    	continue
	    else:
	    	t.append(word)
t.sort()
print(t)

ans = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

if t == ans: print("correct!!!!!!\n")