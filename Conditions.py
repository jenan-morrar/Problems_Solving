"""
Given an integer,n,perform the following conditional actions:
- If  is odd, print Weird
- If  is even and in the inclusive range of 2 to 5, print Not Weird
- If  is even and in the inclusive range of 6 to 20, print Weird
- If  is even and greater than 20, print Not Weird
"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input("Please Enter integer number: ").strip())
if 1 <= n <= 100:
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        if 6 <= n <= 20:
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")
