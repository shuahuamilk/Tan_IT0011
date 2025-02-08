first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenation
full_name = first_name + " " + last_name

# Slicing the first three characters of first name
sliced_name = first_name[:3]

# String formatting
greeting_message = "Hello, {}! Welcome!".format(sliced_name)

# Display output
print("Full Name:", full_name)
print(greeting_message)