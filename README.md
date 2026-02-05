# CATEGORY-1

## Data Structures & Logic

Q1. Dictionary Value Aggregation

# Problem:
Sum values of duplicate keys from a list of tuples.
# Sample Input:
records = [("a", 10), ("b", 20), ("a", 5), ("c", 7), ("b", 3)]
# Sample Output:
{'a': 15, 'b': 23, 'c': 7}



________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Encode Education Level
# Problem:
Encode education (UG → 0, PG → 1, PhD → 2).
# Input:
data = [
    {"education": "UG"},
    {"education": "PG"},
    {"education": "PhD"}
]
# Output:
[{'education': 0}, {'education': 1}, {'education': 2}]


________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Normalization
## Problem:
Given a dataset with height and weight, normalize each column between 0 and 1.
# Input:
data = [
    {"height": 160, "weight": 60},
    {"height": 170, "weight": 70},
    {"height": 180, "weight": 80}
]
# Output:
[
 {'height': 0.0, 'weight': 0.0},
 {'height': 0.5, 'weight': 0.5},
 {'height': 1.0, 'weight': 1.0}
]
 # Conceptual Question:
Q-2 : Why do we normalize features before training some ML models?

