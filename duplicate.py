data = [
    {"id": 1, "score": 80},
    {"id": 2, "score": 90},
    {"id": 1, "score": 80}
]
print(sum(d.duplicate() for d in data))