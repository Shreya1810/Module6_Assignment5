# Task 1: Create a Dictionary of Student Marks
student_dict = {"Shreya": 99, "Vaibhav": 99.5, "xyz":87, "Naira": 58}

student_name = input("Enter student's name: ")
if student_name in student_dict.keys():
    print(f"{student_name}'s marks is {student_dict[student_name]}")
else:
    print("Student not found.")