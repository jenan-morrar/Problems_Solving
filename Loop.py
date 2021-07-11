"""
The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, print i^2.
"""

if __name__ == "__main__":
    num = int(input("Please enter an integer number: "))
    for i in range(0,num):
        print(i**2)