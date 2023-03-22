import sys
#open and read file
allLine = []
temp = []
with open (sys.argv[1],"r") as f:
	mylist = [line.rstrip('\n') for line in f]
	for line in mylist:
		temp.append(line)
		temp += line.split(' ',2)
		temp += line.split('@',1)
		allLine.append(temp)
		temp = []
#print(allLine[0])
requete = sys.argv[2]
#print(requete)
requete = requete.split(' ',2)
#print(requete)	
r1 = requete[0]
if (r1 == '?'):
    r1 = ''
r2 = requete[1]
if (r2 == '?'):
    r2 = ''
r3 = requete[2]
if (r3[0] == '?'):
    r3 = r3.replace('?','')
#print(r1)
#print(r2)
#print(r3)

#find and print
found = []
for find in allLine:
    if ((r1 in find[1]) & (r2 in find[2]) & (r3 in find[3])):
       found.append(find[0])

for line in found:
    print(line)

sys.stderr.write(str(len(found))+ " results\n\n")
