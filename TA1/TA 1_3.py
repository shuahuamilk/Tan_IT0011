# Program 3a:
def pattern_a(rows=5):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "".join(str(j) for j in range(1, i + 1)))

# Program 3b:
def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 == 1:
            print(" " * ((7 - i) // 2) + str(i) * i)
        i += 2

pattern_a()
pattern_b()
