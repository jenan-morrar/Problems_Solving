"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution(object):
 def longestCommonPrefix(self, string_lst):
    if len(string_lst) == 0:
        return ""
    current = string_lst[0]
    for i in range(1, len(string_lst)):
        temp = ""
        if len(current) == 0:
            break
        for j in range(len(string_lst[i])):
            if j < len(current) and current[j] == string_lst[i][j]:
                temp += current[j]
            else:
                break
        current = temp
    return current


if __name__ == "__main__":
    string_lst = []
    size = int(input("Please enter the size of the list: "))
    for i in range (0,size):
        string_lst.append(input("Please enter a string: "))

    SolutionObject = Solution()
    print(SolutionObject.longestCommonPrefix(string_lst))