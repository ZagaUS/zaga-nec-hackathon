import pandas as pd
data = [
    {"age": 25, "name": "A", "salary": 50000}
]
df=pd.DataFrame(data)
df=df.select_dtypes(include='number')
print(df)