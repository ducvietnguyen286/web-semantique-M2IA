import sys

#open and read file
allLine = []
temp = []
with open (sys.argv[1],"r") as f:
	for line in f:
		temp.append(line)
		temp += line.split(' ',2)
		allLine.append(temp)
		temp = []
print(allLine[1])



#nhap r1 2 3 tuong ung voi cac gia tri ? ? ?

r1 = sys.argv[2]           #request s
if (r1 == '?'):
    r1 = ''
r2 = sys.argv[3]           #request p
if (r2 == '?'):
    r2 = ''
r3 = sys.argv[4]           #request o
if (r3[0] == '?'):
	r3 = r3.replace('?','')
 

#find and print
found = []
for find in allLine:
    if ((r1 in find[1]) & (r2 in find[2]) & (r3 in find[3])):
       found.append(find[0])

#viet----------------------------------------------------------
#for fin in allLine:
#	if(r1 in find[1]) & (r2 in find[2])):

#--------------------------------------------------------------
for line in found:
    print(line)

sys.stderr.write(str(len(found))+ " results")