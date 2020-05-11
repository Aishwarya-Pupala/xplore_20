# page 4


class Employee:
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_salary=emp_salary
        
    def increase_salary(self,inp_percent):
        self.emp_salary+=(inp_percent/100)*self.emp_salary
   
        
class Organisation(Employee):
    def __init__(self,org_name,emp_list):
        self.org_name=org_name
        self.emp_list=emp_list
        
        
    def calculate_increment(self,inp_role,inp_percent):
        emp_res=[]
        for emp in self.emp_list:
            if emp.emp_role==inp_role:
                emp.increase_salary(inp_percent)  
                emp_res.append(emp)
        return emp_res
                
        

if __name__=='__main__':
    emp_list=[]
    count=int(input())
    for i in range(count):
        eid=int(input())
        name=input()
        role=input()
        salary=int(input())
        emp_list.append(Employee(eid,name,role,salary))
        
    o=Organisation("XYZ Corp", emp_list)
    
    inp_role=input()
    inp_percent=int(input())
    result=o.calculate_increment(inp_role,inp_percent)
    if len(result)!=0:
        for emp in result:
            print(emp.emp_name,'\t',emp.emp_salary)
    else:
        print("No employee found with the given role")
        
        
        
        
        
# 3
# 1
# ash
# dev
# 1000
# 2
# pra
# uid
# 2000
# 3
# anu
# dev
# 1000
# dev
# 5        
#           
#          
#          
        
        
        
        
        
        
        