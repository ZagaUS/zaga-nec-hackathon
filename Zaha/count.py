from collections import defaultdict
def a(data):
    missing_counts = defaultdict(int)
    for row in data:
        for column, value in row.items():
            if value is None:
                missing_counts[column] += 1
    return dict(missing_counts)
data = [
    {"age": None, "salary": 50000},
    {"age": 30, "salary": None}
]
output = a(data)
print(output)

