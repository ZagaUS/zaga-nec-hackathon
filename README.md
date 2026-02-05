# CATEGORY-1

## Data Structures & Logic

Q1. Find Common Elements (No Duplicates)
# Problem:
Find common elements between two lists without duplicates.
# Sample Input:
a = [10, 20, 30, 40, 50, 20]
b = [30, 60, 20, 70]
# Sample Output:
[20, 30]


________________________________________
# CATEGORY-2

## Coding for ML Context

Q1. Fill Missing Scores with Median
# Problem:
Replace missing scores with median score.
# Input:
data = [
    {"score": 85},
    {"score": None},
    {"score": 90},
    {"score": 75}
]
# Output:
[{'score': 85}, {'score': 85.0}, {'score': 90}, {'score': 75}]

________________________________________

# CATEGORY-3

## ML Fundamentals

Question 1 – One-Hot Encoding
# Problem:
You have a dataset of products with category and price.
Convert the category column into one-hot encoded features.
# Input:
data = [
    {"category": "Electronics", "price": 1200},
    {"category": "Clothing", "price": 500},
    {"category": "Electronics", "price": 1500},
    {"category": "Furniture", "price": 700}
]
# Output:
[
 {'price': 1200, 'Electronics': 1, 'Clothing': 0, 'Furniture': 0},
 {'price': 500, 'Electronics': 0, 'Clothing': 1, 'Furniture': 0},
 {'price': 1500, 'Electronics': 1, 'Clothing': 0, 'Furniture': 0},
 {'price': 700, 'Electronics': 0, 'Clothing': 0, 'Furniture': 1}
]
## Conceptual Question:
Q2: What is the advantage of one-hot encoding over label encoding for categorical variables?
