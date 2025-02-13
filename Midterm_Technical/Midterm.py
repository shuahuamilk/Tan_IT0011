import os
from datetime import datetime
#1
#ensures correct file path.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "numbers.txt")

#checks if a number is a palindrome.
def is_palindrome(n):
    return str(n) == str(n)[::-1]  #converts the number to string and compare with its reverse.

#reads numbers from the file and check for the sum of the palindrome.
def check_palindrome_from_file(filename):
    try:
        #open & reasd all lines.
        with open(filename, 'r') as file:
            lines = file.readlines()

        #process each line in the file.
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))  #convert comma values to int.
            total = sum(numbers)  #sum of numbers.
            status = "Palindrome" if is_palindrome(total) else "Not a palindrome"  #check if total is palindrome.
            #prints correct format.
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {status}")

    except FileNotFoundError:
        print("Error: numbers.txt file not found. Please ensure it is in the same folder as the script.")
#2
#translate a date toreadable format
def translate_date(date_str):
    try:
        #converts the input string into a datetime format
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")

        #formats to correct datetime
        print("Date Output:", date_obj.strftime("%B %d, %Y"))

    except ValueError:
        print("Invalid date format. Please enter in mm/dd/yyyy format.")

#run program 1
print("\n--- Sum Palindrome Checker ---")
check_palindrome_from_file(file_path)

#run program 2
print("\n--- Date Format Translator ---")
user_date = input("Enter the date (mm/dd/yyyy): ") 
translate_date(user_date) #converion
