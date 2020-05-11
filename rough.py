3
1
bread
30
5
2
milk
50
10
3
cookies
100
2
3
bread
2
butter
1
milk
2





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
    
    
    

    