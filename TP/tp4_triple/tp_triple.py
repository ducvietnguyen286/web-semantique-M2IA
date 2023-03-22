import sys
import xml.dom.minidom
#Function replace prefix by Namespace
def addNS(prefix_namespace, spo):
    for y in prefix_namespace:
        spo = spo[0:len(y[0])].replace(y[0], y[1], 1) + spo[len(y[0]):]  # replace only prefix
    return spo
