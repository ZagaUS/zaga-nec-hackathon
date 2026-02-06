data = [
    {"salary": 40000},
    {"salary": 50000},
    {"salary": 60000}
]
for d in data:
    if d["salary"] > 45000:
        d["high_salary"] = True
    else:
        d["high_salary"] = False
print(data)