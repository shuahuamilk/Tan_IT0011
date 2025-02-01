# Program 1:
def count_characters():
    input_string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spaces = 0
    vowel_count = 0
    consonant_count = 0
    other_count = 0
    #Char Loop
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            spaces += 1
        else:
            other_count += 1
    #Prints the output
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}, Spaces: {spaces}, Other characters: {other_count}")

count_characters()