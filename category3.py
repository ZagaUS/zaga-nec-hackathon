import pandas as pd
data = [
    {"age": 25, "country": "IN"},
    {"age": 30, "country": "IN"},
    {"age": 35, "country": "IN"}
]
df = pd.DataFrame(data)
df['age'] = df['age'].fillna(df['age'].median())
print(df['country'].mode()[0])