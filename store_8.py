#21
class Item:
    def __init__(self,item_id,item_name,item_price,available_quantity):
        self.item_id=item_id
        self.item_name=item_name
        self.item_price=item_price
        self.available_quantity=available_quantity
      
    def calculate_price(self,n): 
     
            #print(it.available_quantity)
            #print(it.item_name)
            if self.available_quantity>=n:
                self.total_price=self.item_price*n
                return self.total_price
            else:
                return 0   
                                        
class Store(Item):
    def __init__(self,ilist):
        self.ilist=ilist
        
    def generate_bill(self,inp): # {a:3;m:4}
        bill_amount=0
        for i,j in inp.items(): 
            for k in ilist:
                if i==k.item_name:
                    tp=k.calculate_price(inp[i])   #method called for "k" object
                    bill_amount+=tp
        return bill_amount
                      
if __name__=='__main__':
    ilist=[]
    icount=int(input())          
    for i in range(icount):  
        id=int(input())
        name=input()             
        quant=int(input())
        price=int(input())
        i=Item(id,name,quant,price)
        ilist.append(i)
        s=Store(ilist)
        
    inp={}
    inp_count=int(input())
    
    for i in range(inp_count):
        name=input()
        quantity=int(input())
        inp[name]=quantity
     
    print(ilist)
    print(inp)    
    print(ilist[0].calculate_price(2))
    print(s.generate_bill(inp))
    
    
# < id,name ,price, avl_qnt    >  
# ilist= [<1,bread,30,5>  ,<2,milk,50,10>  ,<3,cookies,100,2>]   
# inp= {bread:2, milk:2  ,butter:1 }    


# 3
# 1
# bread
# 30
# 5
# 2
# milk
# 50
# 10
# 3
# cookies
# 100
# 2
# 3
# bread
# 2
# butter
# 1
# milk
# 2

    
    