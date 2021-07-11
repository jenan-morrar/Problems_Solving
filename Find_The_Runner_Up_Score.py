#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score. You are given  scores.
#Store them in a list and find the score of the runner-up.

if __name__ == "__main__":
    n = int(input("Please Enter Integer Number: "))
    arr = map(int, input("Please Enter Array Elements: ").split())

    arr = list(set(list(arr)))
    arrayLength = len(arr)
    arr = sorted(arr)
    print(arr[arrayLength - 2])
