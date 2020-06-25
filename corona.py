class Corona:
    def __init__(self,stateId,stateName,csd):
        self.stateId=stateId
        self.stateName=stateName
        self.csd=csd
        
        
class Func:
    def __init__(self,l):
        self.l=l
   
    def totalcases(self,sid):
        for i in self.l:
            if sid==i.stateId:
                return sum(i.csd.values())
           
        return 0
    

    def highestcases(self):
        hc={}
        for i in self.l:
            tc=pp.totalcases(i.stateId)
            hc[i.stateName]=tc
        k=max(hc.values())
        print(hc)
        for i,j in hc.items():
            if j==k:
                return(i,j)
              
        return 0    
            

if __name__=='__main__':
    l=[]
    c=int(input())
    for i in range(c):
        csd={}
        stateId=int(input())
        stateName=input()
        for j in range(2):
            sn=input()
            tot=int(input())
            csd[sn]=tot
        ob=Corona(stateId,stateName,csd) 
        l.append(ob)   
    
  
    pp=Func(l)
    sid=int(input())
    r1=pp.totalcases(sid)
    if r1!=0:
        print("Total cases for the state with state id {} is {}".format(sid,r1))
    else:
        print("No state with the given state id exists")
        
    r2=pp.highestcases()
    if r2!=0:
        print("State with highest number of cases is {} with {} no. of cases".format(r2[0],r2[1]))
    else:
        print("No Highest no. of cases")
            



OUTPUT

2
1
maha
raigad
20
thane
30
2
Delhi
abc
50
pqr
10
1
Total cases for the state with state id 1 is 50
{'maha': 50, 'Delhi': 60}
State with highest number of cases is Delhi with 60 no. of cases

