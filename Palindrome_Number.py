"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
"""

def is_Palindrome(num):
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Please enter number: "))
    if (is_Palindrome(num) == True):
        print("it is a palindrome")
    else:
        print("It is not a palindrome")
