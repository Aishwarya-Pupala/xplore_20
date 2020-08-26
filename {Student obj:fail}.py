class Student:
   
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        
    def  calculateResult(self):
        average=0
        if self.sub1>40 and self.sub2>40 and self.sub3>40:
            average=(self.sub1+self.sub2+self.sub3)/3
            return average
        return 0
    
class School:
    def __init__(self,sname,sd):
        self.sname=sname
        self.sd=sd
        
    def getResult(self):
        for k,v in self.sd.items():
            res=k.calculateResult()
            if res>60:
                sd[k]="pass"
        return sd 
        
    def getmarks(self):     
        l=[]
        for k,v in self.sd.items():
            res=k.calculateResult()
            l.append(res)
        high=max(l)
        ll=[]
        for k,v in self.sd.items():
            avg=0
            avg=(k.sub1+k.sub2+k.sub3)/3
            if avg==high:
                ll.append(k)
        if(len(ll)!=0):
           return ll
        return None  
           
if __name__=='__main__':
    sd={}
    n=int(input())
    for i in range(n):
        name=input()
        sub1=float(input())
        sub2=float(input())
        sub3=float(input())
        ob1=Student(name,sub1,sub2,sub3)
        sd[ob1]="fail"
    
    sname=input()
    ob2=School(sname,sd)
    r1=ob2.getResult()
    r2=ob2.getmarks()
    
    
    for k,v in r1.items():
        if r1[k]=="pass":
            print(k.name)
     
    if r2!=None:
        for i in r2:
            print(i.name)
        
    else:
        print("No Student Passed")  
    
3
armaan
40
55
60
shivam
55
78
90
jai
60
77
94
DPS  
