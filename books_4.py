class Book:  #15
    def __init__(self,bid,bname):
        self.book_id=bid
        self.book_name=bname
    
class Library:
    def __init__(self,library_id,address,blist):
        self.library_id=library_id
        self.address=address
        self.book_list=blist
    
    def count_books(self,char):
        c=0
        for i in self.book_list:      
           if i.book_name.startswith(char)==True:
                c+=1                 
        return c
    
    def remove_books(self,blist):
        for book in blist:
            for b in self.book_list:
                if book==b.book_name:
                    self.book_list.remove(b)
              
if __name__=='__main__':
    books=[]                       
    count=int(input())
    for i in range(count):
        bid =int(input())
        bname=input()
        b=Book(bid,bname)
        books.append(b)
        
    l=Library(123,'Mumbai',books)
    char=input()
    ccount=int(input())
    names=[]
    
    for i in range(ccount):
        names.append(input())
    print(l.count_books(char))
    
    l.remove_books(names)
    
    for i in l.book_list:
        print(i.book_name)
            
# 3
# 100
# core
# 200
# sql
# 300
# c++
# c
# 3
# odyssey
# java
# hello world        
        
        
        
        
        