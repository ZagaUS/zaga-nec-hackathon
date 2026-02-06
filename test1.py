import pandas as pd
data = [
    {"score": 80, "passed": "Yes"},
    {"score": None, "passed": "No"},
    {"score": 90, "passed": "Yes"},
    {"score": 70, "passed": "No"}
]
df=pd.DataFrame(data)
df['score'] = df['score'].fillna(df['score'].median())
df['passed']=df['passed'].map({'Yes':1,'No':0})
print(df)