data = [
    {"name": "Alice", "job_role": "Engineer"},
    {"name": "Bob", "job_role": None},
    {"name": "Charlie", "job_role": "Analyst"},
    {"name": "David", "job_role": "Engineer"}
]
for d in data:
    d.update({
        'job_role': d['job_role'] if d['job_role'] is None else {
            'Engineer':0,
            'Analyst':1,
            None:2
        }[d['job_role']]
    })
print(data)