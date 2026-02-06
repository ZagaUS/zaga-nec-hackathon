text = "AIandMLAreFUN"
countupper=0
countlower=0
for i in text:
    if i.isupper():
        countupper+=1
    elif i.islower():
        countlower+=1
print("Number of uppercase letters:", countupper)
print("Number of lowercase letters:", countlower)