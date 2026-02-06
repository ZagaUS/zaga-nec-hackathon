def keepnumvalue(data):
    result = []
    for record in data:
        num_record = {k: v for k, v in record.items() if isdigit(v, (int, float))}
        result.append(num_record)
    return result

data = [
    {"age": 25, "name": "A", "salary": 50000}
]
print(keepnumvalue(data))