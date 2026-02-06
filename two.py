import pandas as pd

data = [
    {"age": 25, "gender": "Male", "salary": 50000},
    {"age": None, "gender": "Female", "salary": 60000},
    {"age": 30, "gender": "Male", "salary": None},
    {"age": 22, "gender": "Female", "salary": 45000}
]

df=pd.DataFrame(data)
#df['salary']=df['salary'].drop()
df['age']=df['age'].fillna(df['age'].mean())
df['gender']=df["gender"].map({"Male":1,"Female":0})
print(df)

