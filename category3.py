data = [
    {"age": 18},
    {"age": 25},
    {"age": 40},
    {"age": 60}
]
ages=[record["age"] for record in data]
min_age=min(ages)
max_age=max(ages)
normalized_ages=[(age-min_age)/(max_age-min_age) for age in ages]
print(normalized_ages)