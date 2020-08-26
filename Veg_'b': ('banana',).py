l=["banana","cherry","grapes","chico","chico"]
l.sort()
d={}
for x in l: #first char
    d[x[0]]=None 

for k in d.keys():
    nl=[]
   # print(k)
    for x in l:
        #print(x[0]).02
        if x[0]==k:
            nl.append(x) 
   # d[k]=nl
   #nl.sort()
  
    t=tuple(nl)  
    d[k]=t
print(d)
    
            
for k in d:
    vl=d[k]
    for n in vl:
        print(n)
        
        
##OUTPUT        
{'b': ('banana',), 'c': ('cherry', 'chico'), 'g': ('grapes',)}
banana
cherry
chico
grapes
