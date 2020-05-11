#19

def check_prime(no):
    if no>1:
        for i in range(2,no):
            if no%i!=0:
                continue
            else:
                return 0
        return 1     
    else:
        return 0
def prime_composite_list(inp):
    prime=[]
    composite=[]
    
    for number in inp:
        check=check_prime(number)
        if check==1:
            prime.append(number)
        if check==0:
            composite.append(number)
            
    return [prime,composite]
        
if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    print(check_prime(inp[1]))
    result=prime_composite_list(inp)
    print(result)
   
# 4
# 11
# 7
# 90
# 44