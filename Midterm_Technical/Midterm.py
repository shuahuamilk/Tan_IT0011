#1
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check_palindrome_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            status = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {status}")
    except FileNotFoundError:
        print("Error: File not found.")

check_palindrome_from_file("numbers.txt")

#2
from datetime import datetime

def translate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        print("Date Output:", date_obj.strftime("%B %d, %Y"))
    except ValueError:
        print("Invalid date format. Please enter in mm/dd/yyyy format.")

# User input
user_date = input("Enter the date (mm/dd/yyyy): ")
translate_date(user_date)
