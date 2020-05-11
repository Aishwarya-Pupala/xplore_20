#9

class Account:
    def __init__(self,account_no,account_name,account_balance):
        self.account_no=account_no
        self.account_name=account_name
        self.account_balance=account_balance
        
    def depositAmnt(self,depamnt):
        self.account_balance=self.account_balance+depamnt
        #return self.account_balance
        
    def withdrawAmnt(self,withamnt):
#             if self.account_balance>=1000:
#                 self.account_balance=self.account_balance-withamnt
#                 return 1
#             else:
#                 return 0
              ab=self.account_balance-withamnt
              if ab>=1000:
                  self.account_balance=ab
                  return 1
              else:
                  return 0
              
            
if __name__=='__main__':
    acno=int(input())
    acname=input()
    acntbal=int(input())
    depamnt=int(input())
    withamnt=int(input())
    
    obj=Account(acno,acname,acntbal)

    obj.depositAmnt(depamnt)
    print("Balance after deposit: ",obj.account_balance)
    
    res=obj.withdrawAmnt(withamnt)
    if res==1:
        print("Balance after withdraw: ",obj.account_balance)
    else:
        print("Insufficient balance for withdrwal")
        
    
# 120
# Rajesh
# 1500
# 1200
# 2000  