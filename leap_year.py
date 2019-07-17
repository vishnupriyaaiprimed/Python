def leapyr(y):
    if (y%100!=0 and y%4==0) or y%400==0:
        return True
    else:
        return False
y=int(input("Enter year:"))
if(leapyr(y)):
    print("Leap Year")
else:
    print("Non leap year")

