# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == "__main__":
    n = int(input("Please Enter Number Of Student: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Please Enter Student Name And Marks").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Please Enter Student Name To Calculate His Average Marks: ")

    output = list (student_marks[query_name])
    avg_marks = sum(output)/len(output)
    print("%.2f" % avg_marks)



