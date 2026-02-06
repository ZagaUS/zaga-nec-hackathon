text = input("Enter a string: ")
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
