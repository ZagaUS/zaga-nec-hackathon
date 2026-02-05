# CATEGORY-1

## Data Structures & Logic

Q1. Count Uppercase and Lowercase Letters
# Problem:
Count uppercase and lowercase letters in a string.
# Sample Input:
text = "AIandMLAreFUN"
# Sample Output:
Uppercase: 7
Lowercase: 6

________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Fill Missing Score and Encode Pass/Fail

## Problem:
1.	Replace missing score with mean score
2.	Encode result (Pass → 1, Fail → 0)
3.	Remove records with missing name
# Input:
data = [
    {"name": "Alice", "score": 85, "result": "Pass"},
    {"name": "Bob", "score": None, "result": "Fail"},
    {"name": None, "score": 90, "result": "Pass"},
    {"name": "Charlie", "score": 70, "result": "Pass"}
]
# Output:
[
 {'name': 'Alice', 'score': 85, 'result': 1},
 {'name': 'Bob', 'score': 78, 'result': 0},
 {'name': 'Charlie', 'score': 70, 'result': 1}
]



________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Normalize Feature Using Min-Max Scaling
## Problem
Normalize the feature age using Min-Max scaling without libraries.
# Input
data = [
    {"age": 18},
    {"age": 25},
    {"age": 40},
    {"age": 60}
]
# Output
[0.0, 0.1667, 0.4583, 1.0]

## Conceptual Question
Q: Why is feature scaling important?






