d1={"a":5,"b":10}
d2={"b":3,"c":7}
s=d1.copy()
for k,v in d2.items():
    if k in s:
        s[k]=s[k]+v
    else:
        s[k]=v
print(s)