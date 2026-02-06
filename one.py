data = ["ml", "ai", "ml", "ds", "ai", "ai"]
c=[]
d=0
if data[0]==data[2]:
    d+=2
    print(d,end=" ")
if data[1]==data[4]==data[5]:
    d+=1
    print(d,end=" ")
    
if data[3]=="ds":
    d=1
    print(d,end=" ")
    print(" ")
for ch in data:
    if ch not in c:
        c.append(ch) 
print(*c)
