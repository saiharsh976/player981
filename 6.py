nimu,pri=map(str,input().split())
if(len(nimu)!=len(pri)):
    print("no")
else:
    s1=[nimu.count(i) for i in nimu]
    s2=[pri.count(i) for i in pri]
if(s1==s2):
    print("yes")
else:
    print("no")
