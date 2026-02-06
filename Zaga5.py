data = [
    {"category": "Electronics", "price": 1200},
    {"category": "Clothing", "price": 500},
    {"category": "Electronics", "price": 1500},
    {"category": "Furniture", "price": 700}
]

categories = sorted(set(d["category"] for d in data))

result = []
for d in data:
    row = {"price": d["price"]}
    for num in categories:
        row[num] = 1 if d["category"] == num else 0
    result.append(row)

print(result)
