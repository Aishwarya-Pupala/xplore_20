class PV:
    def __init__(self,vs,fw,pf,vp):
        self.vs=vs
        self.fw=fw
        self.pf=pf
        self.vp=vp
        self.ps="Parked"
    
class PL:
    def __init__(self,pvd):
        self.pvd=pvd
    
    def ups(self,ln):
        if ln not in self.pvd:
            return None
        else:
            self.pvd[ln].ps="Cleared"
            return (ln,self.pvd[ln].ps)

    def gpc(self,ln):
        tc=0
        if ln not in self.pvd:
            return None
        if self.pvd[ln].fw=="Yes":
            tc=self.pvd[ln].pf*50
        else:
            tc=self.pvd[ln].pf*30
        if self.pvd[ln].vp=="Yes":
            tc+=10
        return tc
    
if __name__=="__main__":
    tpvo=int(input())
    pvd={}
    for i in range(tpvo):
        vs=int(input())
        fw=input()
        pf=float(input())
        vp=input()
        ltn=int(input())
        pvo=PV(vs,fw,pf,vp)
        pvd.update({ltn:pvo})
    ltns=int(input())
    plo=PL(pvd)
    p=plo.ups(ltns)
    q=plo.gpc(ltns)
    if p==None or q==None:
        print("Lot Number Invalid")
    else:
        print(p[0],p[1])
        print(q)
