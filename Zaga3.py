data = [
    {"score": 85},
    {"score": None},
    {"score": 90},
    {"score": 75}
]

scores = sorted(d["score"] for d in data if d["score"] is not None)
n = len(scores)
median = scores[n//2] if n % 2 != 0 else (scores[n//2 - 1] + scores[n//2]) / 2

for d in data:
    if d["score"] is None:
        d["score"] = (median)

print(data)
