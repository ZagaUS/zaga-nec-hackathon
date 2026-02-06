import pandas as pd 
df=pd.read_csv("data.csv")
print(df.head())

df(set(mean(data)))
data = [
    {"age": 25, "height": 170, "weight_status": "Normal"},
    {"age": 30, "height": None, "weight_status": "Overweight"},
    {"age": None, "height": 165, "weight_status": "Normal"},
    {"age": 22, "height": 160, "weight_status": "Normal"}
]
print(mean(set((data))))
