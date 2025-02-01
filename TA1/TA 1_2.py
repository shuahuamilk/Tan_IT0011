# Program 2:
def sum_of_digits():
    input_string = input("Enter a string containing digits: ")
    total = 0
    for char in input_string:
        if char.isdigit():
            total += int(char)
    print(f"Sum of digits: {total}")

sum_of_digits()
