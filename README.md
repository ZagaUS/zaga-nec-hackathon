# CATEGORY-1

## Data Structures & Logic
Q1. Find Missing Numbers in a Range
# Problem:
Given a list of integers, find the missing numbers between the minimum and maximum values.
# Sample Input:
nums = [3, 7, 1, 2, 8, 4]
# Sample Output:
[5, 6]

________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Fill Missing Score with Median and Encode Pass Column
## Problem:
1.	Replace missing score with median score
2.	Encode passed column (Yes → 1, No → 0)
# Input:
data = [
    {"score": 80, "passed": "Yes"},
    {"score": None, "passed": "No"},
    {"score": 90, "passed": "Yes"},
    {"score": 70, "passed": "No"}
]
# Output:
[
 {'score': 80, 'passed': 1},
 {'score': 80, 'passed': 0},
 {'score': 90, 'passed': 1},
 {'score': 70, 'passed': 0}
]


________________________________________

# CATEGORY-3

## ML Fundamentals
Question 1 – Count Encoding
# Problem:
Given a column city, replace each city with the count of its occurrence.
# Input:
data = [
    {"city": "NY"},
    {"city": "LA"},
    {"city": "NY"},
    {"city": "SF"}
]
# Output:
[
 {'city': 2},
 {'city': 1},
 {'city': 2},
 {'city': 1}
]
# Conceptual Question:	
Q: What is count encoding and when is it useful?