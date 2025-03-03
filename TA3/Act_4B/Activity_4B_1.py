# Define sets A, B, and C
A = {"a", "b", "c", "d", "e", "f", "g"}
B = {"d", "e", "f", "g", "h", "i", "j", "k"}
C = {"f", "g", "h", "i", "l", "m", "n", "o"}

# a. Number of elements in A ∪ B
print(f"Number of elements in A and B: {len(A | B)}")

# b. Number of elements in B that are not in A or C
print(f"Elements in B but not in A or C: {len(B - (A | C))}")

# c. Specific set operations
print(f"i. [h, i, j, k]: {B - (A | C)}")
print(f"ii. [c, d, f]: {(A & B) - C}")
print(f"iii. [b, c, h]: {(A | C) - B}")
print(f"iv. [d, f]: {A & B & C}")
print(f"v. [c]: {A - (B | C)}")
print(f"vi. [l, m, o]: {C - (A | B)}")
