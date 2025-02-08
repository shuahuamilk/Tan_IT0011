# Read students.txt file
try:
    with open("students.txt", "r") as file:
        contents = file.read()
        print("Student Information:")
        print(contents)
except FileNotFoundError:
    print("The file 'students.txt' does not exist.")