# CATEGORY-1

## Data Structures & Logic
Q1. Find Element with Maximum Frequency
# Problem:
Print the element that appears the most in a list.
# Sample Input:
nums = [4, 1, 2, 2, 3, 2, 4, 4, 4]
# Sample Output:
4

________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Encode Yes/No and Fill Missing Experience
## Problem:
1.	Replace missing experience with median experience
2.	Encode remote_work (Yes → 1, No → 0)
3.	Remove records with missing department
# Input:	
data = [
    {"department": "IT", "experience": 3, "remote_work": "Yes"},
    {"department": "HR", "experience": None, "remote_work": "No"},
    {"department": None, "experience": 5, "remote_work": "Yes"},
    {"department": "IT", "experience": 2, "remote_work": "No"}
]
# Output:
[
 {'department': 'IT', 'experience': 3, 'remote_work': 1},
 {'department': 'HR', 'experience': 3, 'remote_work': 0},
 {'department': 'IT', 'experience': 2, 'remote_work': 0}
]

________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Identify Constant Features
## Problem
Identify features with no variance.
# Input
data = [
    {"age": 25, "country": "IN"},
    {"age": 30, "country": "IN"},
    {"age": 35, "country": "IN"}
]
# Output
['country']

# Conceptual Question
Q: Why remove constant features?



