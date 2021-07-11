"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
open_list = ["[","{","("]
close_list = ["]","}",")"]
def is_vaildParentheses(parentheses):
    list = []
    for i in parentheses:
        if i in open_list:
            list.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(list) > 0) and
                    (open_list[pos] == list[len(list) - 1])):
                list.pop()
            else:
                return False
    if len(list) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    parentheses = input("Please enter a Parentheses: ")
    if (is_vaildParentheses(parentheses)):
        print("Valid Parentheses")
    else:
        print("Invalid Parentheses")