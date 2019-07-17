import re
str=input()
m=re.sub('[^&]&&[^&]',' and ',str)
str=re.sub('[^\|]\|\|[^\|]',' or ',m)
print(str)
