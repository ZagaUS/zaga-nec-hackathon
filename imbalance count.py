from collections import Counter
text = [
    {"customer_id": 101, "churn": 1},
    {"customer_id": 102, "churn": 0},
    {"customer_id": 103, "churn": 1},
    {"customer_id": 104, "churn": 0},
    {"customer_id": 105, "churn": 1}
]
text_counter = Counter(entry['churn'] for entry in text)
print(text_counter)