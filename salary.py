import pandas as pd
data = [
    {"salary": 40000},
    {"salary": 60000},
    {"salary": 80000}
]
df = pd.DataFrame(data)
df["salary"] = df['salary'] - df['salary'].min() / df['salary'].min() - df['salary'].m()
print(df["salary"].tolist())
