ar=[10,20,30,40,50]
k=3
res=[]
n=len(ar)
for i in range(k,n):
    res.append(ar[i])
for i in range(k):
    res.append(ar[i])
print(res)
# ---------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
data = [
    {"age": 25, "name": "A", "salary": 50000}
]
df=pd.DataFrame(data)
df=df.select_dtypes(include='number')
print(df)
# ---------------------------------------------------------------------------------------------------------------------------------
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


