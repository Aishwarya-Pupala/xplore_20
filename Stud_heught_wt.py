
class Student:
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight



class Details:
   
    def __init__(self,d):
        self.d=d
        
    def moreHeight(self):
        max=0
        print(self.d)
        for k,v in self.d.items():
            
            if self.d[k].height>max:
                max=d[k].height          
        return max
                

if __name__=='__main__':
    d={}
    for i in range(2):
        height=int(input())
        weight=int(input())
        det=Student(height,weight)
        d[i]=det
        
    ob=Details(d)
    r1=ob.moreHeight()
    print(r1)   
    
6
20
3
10

{0: <__main__.Student object at 0x02FF8350>, 1: <__main__.Student object at 0x02FF82F0>}
6
