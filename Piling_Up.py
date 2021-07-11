"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j]>= sideLength{i} .
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print Yes if it is possible to stack the cubes. Otherwise, print No.

**Sample Input**
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

**Sample Output**
Yes
No

"""

if __name__ in '__main__':
    t = int(input("Please Enter Number Of Lists"))
    for i in range(0, t):
        n = int(input("Please enter number of elements: "))
        lst = list(map(int, input("Please enter the elements: ").split()))
        min_index = lst.index(min(lst))
        left = lst[ : min_index]
        right = lst[min_index : ]
        if left == sorted(left, reverse = True) and right == sorted(right, reverse = False):
            print("Yes")
        else:
            print("No")
