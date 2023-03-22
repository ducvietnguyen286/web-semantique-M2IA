
##########################################################################################################################                          
from xml.dom import minidom
import sys
doc = minidom.parse(sys.argv[1])

def Att_value(doc):
   Rac=doc.childNodes[0]   
   return Rac
   
    

def a1(f,Rac):
    akL=list(Rac.attributes.keys()) 
    F=f.childNodes
    nF =filsnt(F)
    n=len(nF)
    if n!=0:
       P=nF[0]
       i=0                            
       if P.nodeName =="rdf:type":
           
           print(remplace(Rac,akL,f.getAttribute("rdf:about")),"a",remplace(Rac,akL,P.getAttribute(list(P.attributes.keys())[0])),findeligne(nF,i))
       else:
           if P.childNodes!=[] and filsnt(P.childNodes)[0].nodeType==3:
              
               print(remplace(Rac,akL,f.getAttribute("rdf:about")),P.nodeName,tagliteraux(P),findeligne(nF,i))   
           elif filsnt(P.childNodes)==[]:
               
               print(remplace(Rac,akL,f.getAttribute("rdf:about")),P.nodeName,remplace(Rac,akL,P.getAttribute(list(P.attributes.keys())[0])),findeligne(nF,i))
           elif filsnt(P.childNodes)[0].nodeType==1:
                        
                        print('      ',P.nodeName+' '+Parse_2(P))    
       for i in range(1,n):
               PP=nF[i]
           
               if PP.nodeName =="rdf:type":
                
                print('      ',"a",remplace(Rac,akL,PP.getAttribute(list(P.attributes.keys())[0])),findeligne(nF,i))
               else:
                   if filsnt(PP.childNodes)!=[] and filsnt(PP.childNodes)[0].nodeType==3:
                      
                      print('      ',PP.nodeName,tagliteraux(PP),findeligne(nF,i))                      
                   elif filsnt(PP.childNodes)==[]:                       
                       
                       print('      ',PP.nodeName,remplace(Rac,akL,PP.getAttribute(list(PP.attributes.keys())[0])),findeligne(nF,i))
                   elif filsnt(PP.childNodes)[0].nodeType==1:
                        
                        print('      ',PP.nodeName+' '+Parse_2(PP))                                       
    else:
        print("[ ] .")                   
                         

def a2(f,Rac):
    akL=list(Rac.attributes.keys()) 
    F=f.childNodes
    nF=filsnt(F)
    n=len(nF)
    P=nF[0]
    i=0
    if P.nodeName =="rdf:type":
       
       print("[ a",remplace(Rac,akL,P.getAttribute(list(P.attributes.keys())[0])),findeligne_2(nF,i))
    else:
        if P.childNodes!=[] and filsnt(P.childNodes)[0].nodeType==3:
           
           return "[ "+P.nodeName+' '+tagliteraux(P)+' '+findeligne_2(nF,i)
        elif filsnt(P.childNodes)==[]:
            
            print("[ ",P.nodeName,remplace(Rac,akL,P.getAttribute(list(P.attributes.keys())[0])),findeligne_2(nF,i))
        elif filsnt(P.childNodes)[0].nodeType==1:
                        
                        print('      ',P.nodeName+' '+Parse_2(P)) 
    for i in range(1,n):
            PP=nF[i]
        
            if PP.nodeName =="rdf:type":
                
                print(" ","a",remplace(Rac,akL,PP.getAttribute(list(P.attributes.keys())[0])),findeligne_2(nF,i))
            else:
                if filsnt(PP.childNodes)!=[] and filsnt(PP.childNodes)[0].nodeType==3:
                               
                   print(" ",PP.nodeName,tagliteraux(PP),findeligne_2(nF,i)) 
                elif filsnt(PP.childNodes)==[]:
                   
                    print(" ",PP.nodeName,remplace(Rac,akL,PP.getAttribute(list(PP.attributes.keys())[0])),findeligne_2(nF,i))
                elif filsnt(PP.childNodes)[0].nodeType==1:
                       
                        print(" ",PP.nodeName+' '+Parse_2(PP))    
        
                    
def a3(f,Rac):
    akL=list(Rac.attributes.keys())    
    F=f.childNodes
    nF =filsnt(F)
    n=len(nF)
    
    print(remplace(Rac,akL,f.getAttribute("rdf:about")),"a",f.nodeName,";")    
    for i in range(n):
           PP=nF[i]
        
           if filsnt(PP.childNodes)!=[] and filsnt(PP.childNodes)[0].nodeType==3:
                       
              print('      ',PP.nodeName,tagliteraux(PP),findeligne(nF,i))
           elif filsnt(PP.childNodes)==[]:
               
               print('      ',PP.nodeName,PP.getAttribute(list(PP.attributes.keys())[0]),findeligne(nF,i))
           elif filsnt(PP.childNodes)[0].nodeType==1:
                        
                        print('      ',PP.nodeName+' '+Parse_2(PP))      
        

def a4(f,Rac):
    F=f.childNodes
    nF =filsnt(F)
    n=len(nF)
    for i in range(n):
        PP=nF[i]
        if i<n:
           if filsnt(PP.childNodes)!=[] and filsnt(PP.childNodes)[0].nodeType==3:
              
              print(f.nodeName,PP.nodeName,tagliteraux(PP),";")
           elif filsnt(PP.childNodes)==[]:
               
               print(f.nodeName,PP.nodeName,PP.getAttribute(list(PP.attributes.keys())[0]),";")
        elif i==n:
             if filsnt(PP.childNodes)!=[] and filsnt(PP.childNodes)[0].nodeType==3:
                
                print(f.nodeName,PP.nodeName,tagliteraux(PP))
             elif filsnt(PP.childNodes)==[]:
                 
                print(f.nodeName,PP.nodeName,PP.getAttribute(list(PP.attributes.keys())[0]))
    
def prefix(Rac):
    L=list(Rac.attributes.keys())    
    for l in L:
        [s,t]=l.split(':',1)
        c="@prefix "+t+':'+'<'+Rac.getAttribute(l)+'>'+' .'
        print(c)


def filsnt_2(F):
    L=[]
    for c in F:
        v=c.nodeValue
        if v is not None and c.nodeValue.isspace():            
               L.append(c)
    return L    


def filsnt_3(F):
    L=[]
    for c in F:
        v=c.nodeValue
        if v is not None and not c.nodeValue.isspace():            
               L.append(c)
    return L    


def filsnt(F):
    L=[]
    for l in F:
       if l not in filsnt_2(F):        
          L.append(l)
    return L       

def remplace(Rac,akL,el):
    for aky in akL:
        [k,l]=aky.split(':',1)
        atval=Rac.getAttribute(aky)
        if atval in el:
           el=el.replace(atval,'')
           nel=l+':'+el 
           return nel
       
def tagliteraux(P):
    if P.attributes!=[] and "rdf:datatype" in list(P.attributes.keys()):
        if "integer" in P.getAttribute("rdf:datatype"):
            return P.childNodes[0].nodeValue
    elif "rdf:datatype" not in list(P.attributes.keys()):
        if "xml:lang" in list(P.attributes.keys()):       
            return '"'+P.childNodes[0].nodeValue+'"'+'@'+P.getAttribute("xml:lang")
        else:
             return '"'+P.childNodes[0].nodeValue+'"'  
         

def findeligne(nF,i):
    n=len(nF)
    if i==0 and n == 1:
       return '.'
    elif i==0 and n >= 2:
        return ';'
    elif i >=1 and i < n-1 and n >= 3:
        return ';'
    elif i == n-1 and n >= 2:     
        return '.' 

def findeligne_2(nF,i):
    n=len(nF)
    if i==0 and n == 1:
       return '] .'
    elif i==0 and n >= 2:
        return ';'
    elif i >=1 and i < n-1 and n >= 3:
        return ';'
    elif i == n-1 and n >= 2:     
        return '] .'    

def recherche(Rac):
    L=[]
    for f in filsnt(Rac.childNodes):
        if filsnt(f.childNodes)==[]:
            L.append(f.nodeName)
        recherche(f)
    print(L)            
     
             
        
                     
def Parse(Rac):
   print('      ') 
   prefix(Rac)
   print('      ')
   FF=filsnt(Rac.childNodes)
   for f in FF:   
      if f.nodeName=='rdf:Description': 
         if "rdf:about" in list(f.attributes.keys()):
            if f.childNodes!=[]:
               
               a1(f,Rac)                
            else:
                print('[  ] .')
         
         elif "rdf:about" not in list(f.attributes.keys()):
             if f.childNodes!=[]:
                
                a2(f,Rac)                            
             else:
                 print('[  ] .')
      
      elif f.nodeName!='rdf:Description':
           if "rdf:about" in list(f.attributes.keys()):             
                 if f.childNodes!=[]:
                     
                     a3(f,Rac)
                 else:
                     print('[  ] .')  
           elif "rdf:about" not in list(f.attributes.keys()) and "rdf:nodeID" not in list(f.attributes.keys()):
              if f.childNodes!=[]:
                 
                 return a4(f,Rac)
              else:
                 print('[  ] .') 
           
           elif "rdf:nodeID" in list(f.attributes.keys()):
               if f.childNodes!=[]:
                   
                   a3(f,Rac)                                             
               else:
                   print('[  ] .')
        
           
          


def Parse_2(Rac):  
   FF=filsnt(Rac.childNodes)  
   for f in FF:
      if f.nodeName=='rdf:Description': 
         if "rdf:about" in list(f.attributes.keys()):
            if f.childNodes!=[]:
               
               return a1(f,Rac)                
            else:
                print('[  ] .')
         
         elif "rdf:about" not in list(f.attributes.keys()):
             if f.childNodes!=[]:
                
                return a2(f,Rac)                            
             else:
                print('[  ] .')
      
      elif f.nodeName!='rdf:Description':
          if "rdf:about" in list(f.attributes.keys()):
                 if f.childNodes!=[]:
                     
                     return a3(f,Rac)
                 else:
                     print('[  ] .')  
          elif "rdf:about" not in list(f.attributes.keys()) and "rdf:nodeID" not in list(f.attributes.keys()):
              if f.childNodes!=[]:
                 
                 return a4(f,Rac)
              else:
                 print('[  ] .')                                
               

Rac=Att_value(doc) 
Parse(Rac)    
    
    
    

    
    
    
    
    
    
    
    