#d={1:hello,2:bolo}


#14


d={}
def count_words(input_string):
    lowercase_s=input_string.lower()
    spt_str=lowercase_s.split()
    for i in spt_str:
        d[i]=0
    for w in spt_str:
        for k,j in d.items():
            if k==w:
                d[k]+=1
    return d

def max_occurence_word(input_string):
    s=input_string.split()
    
    for cnt in d.values():
        m=max(d.values())
        
        for i,j in d.items():
            if j==m:
                return i

if __name__=='__main__':
    input_string=input()
    dict=count_words(input_string)
    st=max_occurence_word(input_string)
    print(dict)
    print(st)
    
    
#     count of each letter->store in dictionary
# test_str = "GeeksforGeeks" 
# all_freq = {} 
#   
# for i in test_str: 
#     if i in all_freq: 
#         all_freq[i] += 1
#     else: 
#         all_freq[i] = 1
#   
# # printing result  
# print ("Count of all characters in GeeksforGeeks is :\n "
#                                         +  str(all_freq)) 