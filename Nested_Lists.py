#Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == "__main__":
    studentGrade = []
    second_lowest_grade = []

#this loop to read nested list from the user

    for _ in range(int(input("Please Enter Number Of Student: "))):
        name = input("Please Enter Student Name: ")
        score = float (input("Please Enter Student Score: "))
        studentGrade.append([name,score])

# this part to sort list and get second lowest grad
    sortedList = sorted(list(set([x[1] for x in studentGrade])))
    second_Lowest = sortedList[1]

# This loop to fetch all student with second lowest grad

    for student in studentGrade:
        if student[1] == second_Lowest:
            second_lowest_grade.append(student[0])

    second_lowest_grade.sort()
    for i in range(0,len(second_lowest_grade)):
        print(second_lowest_grade[i])