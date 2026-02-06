# CATEGORY-1

## Data Structures & Logic

Q1. Rotate List by K Positions
# Problem:
Rotate a list to the right by k positions.
# Sample Input:
arr = [10, 20, 30, 40, 50]
k = 2
# Sample Output:
[40, 50, 10, 20, 30]




________________________________________
# CATEGORY-2

## Coding for ML Context
Q1. Feature Selection
# Problem:
Keep only numeric features.
# Input:
data = [
    {"age": 25, "name": "A", "salary": 50000}
]
# Output:
[{'age': 25, 'salary': 50000}]





________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Handling Missing Categorical Values
# Problem:
You are given a dataset of customers with job_role. Fill missing job_role with "Unknown" and encode as integers (assign unique integer per category).
# Input:
data = [
    {"name": "Alice", "job_role": "Engineer"},
    {"name": "Bob", "job_role": None},
    {"name": "Charlie", "job_role": "Analyst"},
    {"name": "David", "job_role": "Engineer"}
]
# Output:
[
 {'name': 'Alice', 'job_role': 0},
 {'name': 'Bob', 'job_role': 2},
 {'name': 'Charlie', 'job_role': 1},
 {'name': 'David', 'job_role': 0}
]
# Conceptual Question:	
Q: Why do we encode categorical variables as integers?




