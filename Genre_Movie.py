class Movie:
    def __init__(self,id,genre,d):
        self.id=id
        self.genre=genre
        self.d=d

class Collections:
    def __init__(self,l):
        self.l=l    
        
    def getMovie(self,gid):
        
        for i in self.l:
            if i.id==gid:
               print(i.d)
               highest=max(i.d.values())
               print(highest)
            for k,v in i.d.items():
                if i.id==gid:
                    if highest==v:
                        return k
        
    def highestgross(self):
         hg=0
         maxxx=None
         for i in self.l:
             s=sum(i.d.values())
             
             if s > hg:
                 maxx=i.genre
                 hg=sum(i.d.values())
         return maxx 
if __name__=='__main__':
    l=[]
    for n in range(2):
        id=int(input())
        genre=input()
        d={}
        for i in range(3):
            name=input()
            coln=int(input())
            d[name]=coln
        m=Movie(id,genre,d)
        l.append(m)
        
    c=Collections(l)
    gid=int(input())
    r1=c.getMovie(gid)
    print(r1)
    r2=c.highestgross()
    print("Genre"+r2)

##OUTPUT
1
action
superman
200
batman
300
spider
350
2
comedy
herapheri
400
golmal
200
welcome
350
2


{'herapheri': 400, 'golmal': 200, 'welcome': 350}
400
herapheri
Genrecomedy

