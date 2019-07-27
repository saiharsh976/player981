sai=list(input())
for i in range(0,len(sai),2):
    sai[i],sai[i+1]=sai[i+1],sai[i]
swap=''.join(sai)
print(swap)
