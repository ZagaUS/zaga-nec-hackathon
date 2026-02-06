import pandas as pd 
data = [
    {"department": "IT", "experience": 3, "remote_work": "Yes"},
    {"department": "HR", "experience": None, "remote_work": "No"},
    {"department": None, "experience": 5, "remote_work": "Yes"},
    {"department": "IT", "experience": 2, "remote_work": "No"}
]
df=pd.DataFrame(data)
median = df['experience'].median()
df['experience']=df['experience'].fillna(median)
df['remote_work']=df['remote_work'].map({'Yes': 1, 'No': 0})
df=df[df['department'].notnull()]
print(df)
