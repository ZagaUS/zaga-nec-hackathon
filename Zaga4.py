data = [
    {"category": "Electronics", "price": 1200},
    {"category": "Clothing", "price": 500},
    {"category": "Electronics", "price": 1500},
    {"category": "Furniture", "price": 700}
]
categorys = set(d["category"] for d in data)
n=len(categorys)
