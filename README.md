# CATEGORY-1

## Data Structures & Logic
Q1. Remove Keys with None Values
# Problem:
Remove all keys with value None from a dictionary.
# Sample Input:
data = {"a": 1, "b": None, "c": 3, "d": None}
# Sample Output:
{'a': 1, 'c': 3}


________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Replace Missing Height with Mean and Encode Weight Status
## Problem:
You are given a dataset. Perform the following:
1.	Replace missing height with mean height
2.	Encode weight_status column (Overweight → 1, Normal → 0)
3.	Remove records where age is missing
	

# Input:
data = [
    {"age": 25, "height": 170, "weight_status": "Normal"},
    {"age": 30, "height": None, "weight_status": "Overweight"},
    {"age": None, "height": 165, "weight_status": "Normal"},
    {"age": 22, "height": 160, "weight_status": "Normal"}
]
# Output:
[
 {'age': 25, 'height': 170, 'weight_status': 0},
 {'age': 30, 'height': 167, 'weight_status': 1},
 {'age': 22, 'height': 160, 'weight_status': 0}
]


________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Calculate Feature Mean by Group
# Problem
Calculate average salary per department.
# Input
data = [
    {"dept": "IT", "salary": 60000},
    {"dept": "HR", "salary": 40000},
    {"dept": "IT", "salary": 80000}
]
# Output
{'IT': 70000, 'HR': 40000}

## Conceptual Question
Q: Why do we create group-based features?

