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

#Result
nTripleList = []
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

# Find S P O from all nodes
for x in fChildList:

    # Find SUBJECT from each paragraph
    sujetAbout = x.getAttribute('rdf:about')  #Get subject from rdf:about
    if len(sujetAbout) > 0:
        # replace prefix by NameSpace
        sujet = "<" + addNS(prefixList, sujetAbout) + ">"
    else:
        # Get subject from rdf:nodeID
        sujet = "_:" + x.getAttribute('rdf:nodeID')

    #Get parametre langue
    langGobal = x.getAttribute('xml:lang')

    # Find PREDICAT and OBJECT for each SUBJECT
    for k in range(1, len(x.childNodes), 2):
        # Get predicat from tagName
        predicatLink = x.childNodes[k].tagName
        # replace prefix by NameSpace
        predicat = "<" + addNS(prefixList, predicatLink) + ">"

        # Get OBJECT from rdf:resource
        objetSource = x.childNodes[k].getAttribute('rdf:resource')
        if len(objetSource) > 0:
            # replace prefix by NameSpace
            objet = "<" + addNS(prefixList, objetSource) + ">"
        else:
            #Get OBJECT from rdf:datatype
            objetDatatype = x.childNodes[k].getAttribute('rdf:datatype')
            if len(objetDatatype) > 0:
                objetType = x.childNodes[k].firstChild.nodeValue  # get value of node
                # replace prefix by NameSpace
                objet = "\"" + str(objetType) + "\"^^<" + addNS(prefixList, objetDatatype) +">"
            else:
                # Get OBJECT from rdf:nodeID
                objetNodeid = x.childNodes[k].getAttribute('rdf:nodeID')
                if len(objetNodeid) > 0:
                    objet = "_:" + objetNodeid
                else:
                    # Get OBJECT from value of node
                    objetLit = x.childNodes[k].firstChild.nodeValue
                    objet = "\"" + objetLit + "\""
                    # Check parametre langue
                    lang = x.childNodes[k].getAttribute('xml:lang')
                    if len(lang) > 0:
                        objet = objet + "@" + lang
                    elif len(langGobal) > 0:
                        objet = objet + "@" + langGobal
        #Get result
        nTripleList.append([sujet,predicat,objet])

#Make n-triple extention
for y in extendList:

    # Find SUBJECT from each paragraph
    sujetAbout = y.getAttribute('rdf:about')  #Get subject from rdf:about
    if len(sujetAbout) > 0:
        # replace prefix by NameSpace
        sujet = "<" + addNS(prefixList, sujetAbout) + ">"
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
    print(res[0] + " " + res[1] + " " + res[2] + " .\n")