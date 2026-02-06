def keepnumvalue(data):
    result = []
    for record in data:
        if isdigit(record):
            result.append(record)
        return result

data = [
    {"age": 25, "name": "A", "salary": 50000}
]
print(keepnumvalue(data))