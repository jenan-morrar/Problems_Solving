"""
* Perform append, pop, popleft and appendleft methods on an empty deque.

**Sample Input**
6
append 1
append 2
append 3
appendleft 4
pop
popleft

**Sample Output**
1 2

"""
from collections import deque


if __name__ == "__main__":

    d = deque()
    for i in range(int(input("Please Enter Number Of Operations: "))):
        operation = input("Please Enter Operation: ").split()
        if operation[0] == 'append':
            d.append(operation[1])
        elif operation[0] == 'appendLeft':
            d.appendleft(operation[1])
        elif operation[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    print(' '.join(d))







