last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
contact_number = input("Enter your contact number: ")
course = input("Enter your course: ")

# Format the collected information
student_info = f"{last_name}, {first_name}, {age}, {contact_number}, {course}\n"

# Open the file in append mode and write the information
with open("students.txt", "a") as file:
    file.write(student_info)

print("Student information has been saved successfully.")