s={1,2,3,4,5,7,8,9}
#sum=10
l=list(s)
l2=[ {l[i],l[j]} for i in range(len(l)) for j in range(i+1,len(l)) if l[i]+l[j]==10]
print(l2)
for i in l2:
    if i.issubset(s):
        print('yes')