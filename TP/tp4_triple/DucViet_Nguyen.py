import sys
from xml.dom import minidom

#Function replace prefix by Namespace
def addNS(prefix_namespace, spo):
    for y in prefix_namespace:
        spo = spo[0:len(y[0])].replace(y[0], y[1], 1) + spo[len(y[0]):]  # replace only prefix
    return spo


tree = minidom.parse(sys.argv[1])  # Parsing file XML
root = tree.firstChild  # Get root of tree XML
nbrFirst = len(root.childNodes)  # Get number of paragraphs

#Number of anonyme node
nb_node_anonyme = 0

#Result
nTripleList = []
turtleList = []
extend = []

# Get NameSpace correspond prefix
prefixList = []
prefix = root.attributes.items()
for m in prefix:
    prefixList.append([(m[0].replace('xmlns:', '') + ':'), m[1]])

#Get list of paragraph
fChildList = []
for i in range(1, nbrFirst, 2):
    fChildList.append(root.childNodes[i])

#Get list of paragraph not rdf:Description
extendList = []
for i in range(1, nbrFirst, 2):
    if (root.childNodes[i].tagName != "rdf:Description"):
        extendList.append(root.childNodes[i])

name_last_anonym = ""
listNodeId = []

def replaceParPrefix(nom):
    if (nom[0] != '<' and nom[1] != '>') :
        return nom
    name_default = nom
    nom = nom[1:-1]
    for prefix in prefixList :
        if (nom.find(prefix[1]) != -1):
            nom = nom.replace(prefix[1],prefix[0])
            if nom == "rdf:type" : return "a"
            return nom.replace(prefix[1],prefix[0])
    return name_default

def parcourir(Child_List):
    global name_last_anonym, nb_node_anonyme
    # Find S P O from all nodes
    for x in Child_List:

        # Find SUBJECT from each paragraph
        sujet_about = x.getAttribute('rdf:about')  #Get subject from rdf:about
        if (len(sujet_about) > 0):
            # replace prefix by NameSpace
            sujet = "<" + addNS(prefixList, sujet_about) + ">"
            if (x.tagName != "rdf:Description"):
                nTripleList.append([sujet, "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<"+addNS(prefixList, x.tagName)+">"])

        else:
            # Get subject from rdf:nodeID
            sujetNodeid = x.getAttribute('rdf:nodeID')
            if (len(sujetNodeid) > 0) :
                sujet = "_:" + x.getAttribute('rdf:nodeID')
                nTripleList.append([sujet, "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<"+addNS(prefixList, x.tagName)+">"])
            else :
                sujet = name_last_anonym

        #Get parametre langue
        langGobal = x.getAttribute('xml:lang')

        #print(x.childNodes)
        # Find PREDICAT and OBJECT for each SUBJECT
        for k in range(1, len(x.childNodes), 2):
            isAnonym = False
            # Get predicat from tagName
            predicatLink = x.childNodes[k].tagName
            # replace prefix by NameSpace
            predicat = "<" + addNS(prefixList, predicatLink) + ">"

            # Get OBJECT from rdf:resource
            objetSource = x.childNodes[k].getAttribute('rdf:resource')
            if (len(objetSource) > 0):
                # replace prefix by NameSpace
                objet = "<" + addNS(prefixList, objetSource) + ">"
            else:
                #Get OBJECT from rdf:datatype
                objetDatatype = x.childNodes[k].getAttribute('rdf:datatype')
                if (len(objetDatatype) > 0):
                    objetType = x.childNodes[k].firstChild.nodeValue  # get value of node
                    # replace prefix by NameSpace
                    objet = "\"" + str(objetType) + "\"^^" + replaceParPrefix("<"+objetDatatype+">")
                else:
                    # Get OBJECT from rdf:nodeID
                    objet_NodeID = x.childNodes[k].getAttribute('rdf:nodeID')
                    if len(objet_NodeID) > 0:
                        objet = "_:" + objet_NodeID
                        if (objet not in listNodeId) : 
                            nTripleList.append([sujet,predicat,objet])
                            listNodeId.append(objet)
                        else :
                            nTripleList.append([objet, "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<"+addNS(prefixList, x.childNodes[k].tagName)+">"])
                        continue

                    elif (x.childNodes[k].childNodes.length == 1 and type(x.childNodes[k].childNodes[0]) == minidom.Text):
                        # Get OBJECT from value of node
                        objetLit = x.childNodes[k].firstChild.nodeValue
                        objet = "\"" + objetLit.strip() + "\""
                        # Check parametre langue
                        lang = x.childNodes[k].getAttribute('xml:lang')
                        if (len(lang) > 0):
                            objet = objet + "@" + lang
                        elif (len(langGobal) > 0):
                            objet = objet + "@" + langGobal
                    else:
                        isAnonym = True
                        nb_Anonyme = len(x.childNodes[k].childNodes)
                        for i in range(1, nb_Anonyme, 2):
                            objet = "_:ns"+str(nb_node_anonyme)
                            nb_node_anonyme+=1
                            name_last_anonym = objet
                            nTripleList.append([sujet,predicat,objet])
                            nTripleList.append([objet, "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<"+addNS(prefixList, x.childNodes[k].childNodes[i].tagName)+">"])
                            ChildListTmp = list()
                            ChildListTmp.append(x.childNodes[k].childNodes[i])
                            parcourir(ChildListTmp)
                        continue
            #Get result
            nTripleList.append([sujet,predicat,objet])

parcourir(fChildList)

#Make n-triple extention
# print("NTRIPLES :")
'''
for y in extendList:
    # Find SUBJECT from each paragraph
    sujet_about = y.getAttribute('rdf:about')  #Get subject from rdf:about
    if len(sujet_about) > 0:
        # replace prefix by NameSpace
        sujet = "<" + addNS(prefixList, sujet_about) + ">"
    else:
        # Get subject from rdf:nodeID
        sujet = "_:" + y.getAttribute('rdf:nodeID')

    # Get Objet from tagName
    objetLink = y.tagName
    # replace prefix by NameSpace
    objet = "<" + addNS(prefixList, objetLink) + ">"

    #Find predicat in nTripleList
    for n in nTripleList:
        if (objet == n[2]):
            extend.append([sujet, n[1], objet])

#Make Final Result
for e in extend:
    if e not in nTripleList:
        nTripleList.append(e)

#Print result
for res in nTripleList:
    print(res[0] + " " + res[1] + " " + res[2] + " .")

#make turtle extention
# print("\nTURTLE : \n")
'''


def regroupAll():
    regroup = dict()
    for triplet in nTripleList :
        if (triplet[0] not in regroup):
            regroup[triplet[0]] = dict()

        if (triplet[1] not in regroup[triplet[0]]):
            regroup[triplet[0]][triplet[1]] = list()
            
        regroup[triplet[0]][triplet[1]].append(triplet[2])

    return regroup


#Print prefix
for prefix in prefixList :
    if prefix[0] != "rdf:" :
        print("@prefix "+ prefix[0] + " <" + prefix[1] + "> .")
print()

turtleDict = regroupAll()
#print(turtleDict)

for turtleSubject in turtleDict:
    print(replaceParPrefix(turtleSubject).strip())

    for turtlePredicat in turtleDict[turtleSubject]:
        print("  "+replaceParPrefix(turtlePredicat).strip(),end="")

        for turtleObject in turtleDict[turtleSubject][turtlePredicat]:
            print(" " + replaceParPrefix(turtleObject).strip('\r\n\t'),end="")
            if (list(turtleDict[turtleSubject].keys()).index(turtlePredicat) == (len(turtleDict[turtleSubject].keys())-1) and (turtleDict[turtleSubject][turtlePredicat].index(turtleObject) == (len(turtleDict[turtleSubject][turtlePredicat])-1))):
                print(" .")
            elif (turtleDict[turtleSubject][turtlePredicat].index(turtleObject) == (len(turtleDict[turtleSubject][turtlePredicat])-1)):
                print(" ;")
            else:
                print(", ",end="")
    print()