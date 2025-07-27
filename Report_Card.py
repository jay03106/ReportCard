# STUDENT REPORT CARD

# Student info
name = input("Enter the name of student: ")
roll = int(input("Enter your roll number: "))
std = int(input("Enter the class: "))

# Subjects and marks
subjects = ['science', 'gujarati', 'hindi']
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Total and average
total = sum(marks)
average = total / len(marks)

# Grade calculation
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Store in dictionary
report_card = {
    'Name': name,
    'Roll Number': roll,
    'Class': std,
    'Marks': marks,
    'Total': total,
    'Average': average,
    'Grade': grade  
}

# Display the report
print("\nReport Card")
print(f"Name         : {report_card['Name']}")
print(f"Roll Number  : {report_card['Roll Number']}")
print(f"Class        : {report_card['Class']}")
print("------------------------------------------")
print(f"Marks        : {report_card['Marks']}")
print(f"Total Marks  : {report_card['Total']}")
print(f"Average Marks: {report_card['Average']:.2f}")
print(f"Grade        : {report_card['Grade']}")


