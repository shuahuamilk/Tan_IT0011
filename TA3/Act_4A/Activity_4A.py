import json
import os

# File to store student records
default_filename = "students.json"

def load_records(filename=default_filename):
    """Load student records from a file."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_records(records, filename=default_filename):
    """Save student records to a file."""
    try:
        with open(filename, "w") as file:
            json.dump(records, file, indent=4)
        print(f"Records saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def show_records(records):
    """Display all student records."""
    print("\nStudent Records:")
    for record in records:
        print(record)

def order_by_last_name(records):
    """Sort students by last name."""
    return sorted(records, key=lambda x: x[1][1].lower())

def order_by_grade(records):
    """Sort students by computed grade (60% Class Standing + 40% Major Exam)."""
    return sorted(records, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)

def show_student(records, student_id):
    """Show details of a specific student."""
    for record in records:
        if record[0] == student_id:
            print("Student Found:", record)
            return
    print("Student not found.")

def add_record(records):
    """Add a new student record."""
    student_id = input("Enter Student ID (6-digit): ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid Student ID. Must be 6 digits.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record(records):
    """Edit an existing student record."""
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ") or record[1][0]
            last_name = input("Enter New Last Name: ") or record[1][1]
            class_standing = float(input("Enter New Class Standing Grade: ") or record[2])
            major_exam = float(input("Enter New Major Exam Grade: ") or record[3])
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student ID not found.")

def delete_record(records):
    """Delete a student record."""
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Student ID not found.")

def save_as_file(records):
    """Save the records to a new file."""
    filename = input("Enter new filename: ")
    save_records(records, filename)
    print("Records saved successfully to", filename)

def main():
    records = load_records()
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            records = load_records()
            print("File loaded successfully.")
        elif choice == "2":
            save_records(records)
            print("File saved successfully.")
        elif choice == "3":
            save_as_file(records)
        elif choice == "4":
            show_records(records)
        elif choice == "5":
            records = order_by_last_name(records)
            show_records(records)
        elif choice == "6":
            records = order_by_grade(records)
            show_records(records)
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student(records, student_id)
        elif choice == "8":
            add_record(records)
        elif choice == "9":
            edit_record(records)
        elif choice == "10":
            delete_record(records)
        elif choice == "11":
            save_records(records)
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
