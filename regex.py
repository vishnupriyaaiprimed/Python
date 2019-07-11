import re
str=input()
m=re.sub('[^&]&&[^&]',' and ',str)
m1=re.sub('[^\|]\|\|[^\|]',' or ',m)
print(m1)
