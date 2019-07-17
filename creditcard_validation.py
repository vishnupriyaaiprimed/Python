import re

n=int(input())
lst=[]
for i in range(n):
    lst.append(input())

for i in range(n):
    match1=re.match(r'^([4-6]\d{3})-(\d{4})-(\d{4})-(\d{4})$',lst[i])
    match2=re.match(r'^([4-6]\d{3})(\d{4})(\d{4})(\d{4})$',lst[i])
    match=match1 or match2
    
    if not match:
        print("Invalid")
    else:
        n=match.group(1)+match.group(2)+match.group(3)+match.group(4)
        for j in range(13):
            if n[j]==n[j+1] and n[j]==n[j+2] and n[j]==n[j+3]:
                    print("Invalid")
                    break
        else:
            print("Valid")
