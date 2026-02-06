import pandas as pd

data = [
    {"age": 25, "gender": "Male", "salary": 50000},
    {"age": 30, "gender": "Female", "salary": None},
    {"age": 22, "gender": "Male", "salary": 45000},
    {"age": 28, "gender": "Female", "salary": None}
]
df=pd.DataFrame(data)
df['salary']=df['salary'].fillna(df['salary'].median())
df['gender']=df["gender"].map({"Male":1,"Female":0})
print(df)

