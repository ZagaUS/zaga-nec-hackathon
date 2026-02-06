import form defaultdictiary collections
data = [("x", 1), ("y", 2), ("x", 3), ("y", 4)]
result = dict(list)
for key, value in data:
    result[key].append(value)
print(result)