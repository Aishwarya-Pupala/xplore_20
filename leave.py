
#10

class Employee:
    def __init__(self,empno,empname,leaves):
        self.empno=empno
        self.empname=empname
        self.leaves=leaves
        
class Company:
    def __init__(self,cname,emps):
        self.cname=cname
        self.emps=emps
    def display_leave(self,empno,ltype):
        for em in self.emps:
            if empno==em.empno:
                for i,j in em.leaves.items():
                    if i==ltype:
                        return j
    def leave_application(self,empno,ltype,nol):
         for em in self.emps:
            if empno==em.empno:
                for i,j in em.leaves.items():
                    if i==ltype:
                        if j>=nol:
                            return "Granted"
                        else:
                            return "Leave Rejected"
                        
        
if __name__=='__main__':
    n=int(input())            #emps=[<eno,ename,{cl:2,el:2,sl:3}>,<>,<>]
    c=Company("ABC",emps=[])
    for i in range(n):
        leaves={}
        eno=int(input())
        ename=input()
        leaves['CL']=int(input())
        leaves["EL"]=int(input())
        leaves["SL"]=int(input())
        e=Employee(eno,ename,leaves)
        c.emps.append(e)
    empno=int(input())
    ltype=input()
    nol=int(input())
    print(c.display_leave(empno,ltype))
    print(c.leave_application(empno,ltype,nol))
        
        
        
        
        
        
        
# 3
# 1
# Rajesh
# 5
# 10
# 3
# 2
# Venakt
# 5
# 20
# 30
# 3
# Brahma
# 10
# 10
# 10
# 3
# EL
# 10      
#     
#     
        