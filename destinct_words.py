
n=int(input())
words=[]
counts=[]
for i in range(n):
    words.append(input())
for i in range(len(words)):
    counts.append(1)
    for j in range(len(words)):
        if(words[i]==words[j]):
            if i<j:
                if counts[len(counts)-1]>0:
                    counts[len(counts)-1]+=1
            elif i>j:
                counts[len(counts)-1]=0
            else:
                pass

while 0 in counts:
    counts.remove(0)

print(len(counts))
for c in counts:
    print(c,end=" ")
