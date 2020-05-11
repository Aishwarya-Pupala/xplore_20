# 2
pal_l=[]
def check_palindrome(inp_str):
    for j in range(count):
        chk_str=inp_str[j]
        rev=chk_str[::-1]
        if rev==inp_str[j]:
            pal_l.append(inp_str[j])
            continue
    return pal_l
    
if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=check_palindrome(inp_str)
    if len(output)!=0:
        for i in output:
            print(i)
    else:
        print("palindrome not found")