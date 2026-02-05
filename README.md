# CATEGORY-1

## Data Structures & Logic

Q1. Frequency Count with Order Preserved
# Problem:
Given a list of strings, print the frequency of each element in the order of first appearance.
# Sample Input:
data = ["ml", "ai", "ml", "ds", "ai", "ai"]
# Sample Output:
ml 2
ai 3
ds 1

________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Handle Missing Age, Encode Gender, Remove Missing Salary
# Problem:
Perform the following preprocessing steps:
1.	Replace missing age with mean age
2.	Encode gender (Male → 1, Female → 0)
3.	Remove records where salary is missing
# Input:
data = [
    {"age": 25, "gender": "Male", "salary": 50000},
    {"age": None, "gender": "Female", "salary": 60000},
    {"age": 30, "gender": "Male", "salary": None},
    {"age": 22, "gender": "Female", "salary": 45000}
]
# Output:
[
 {'age': 25, 'gender': 1, 'salary': 50000},
 {'age': 23.5, 'gender': 0, 'salary': 60000},
 {'age': 22, 'gender': 0, 'salary': 45000}
]
________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – Missing Value Imputation
# Problem:
You are given a dataset of customers as a list of dictionaries with age, gender, and salary.
Replace missing salary with the median salary and encode gender (Male → 1, Female → 0).
# Input:
data = [
    {"age": 25, "gender": "Male", "salary": 50000},
    {"age": 30, "gender": "Female", "salary": None},
    {"age": 22, "gender": "Male", "salary": 45000},
    {"age": 28, "gender": "Female", "salary": None}
]
# Output:
[
 {'age': 25, 'gender': 1, 'salary': 50000},
 {'age': 30, 'gender': 0, 'salary': 47500},
 {'age': 22, 'gender': 1, 'salary': 45000},
 {'age': 28, 'gender': 0, 'salary': 47500}
]
### Conceptual Question:
Question 2 - Why do we use median instead of mean for missing value imputation?
