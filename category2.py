import pandas as pd
data = {
    "name": ["Alice", "Bob", None, "Charlie"],
    "score": [85, None, 90, 70],
    "result": ["Pass", "Fail", "Pass", "Pass"]
}
df = pd.DataFrame(data)
df["score"] = df["score"].fillna(df["score"].mean())
df["result"] = df["result"].map({"Pass": 1, "Fail": 0})
df = df.dropna(subset=["name"])
print(df)
