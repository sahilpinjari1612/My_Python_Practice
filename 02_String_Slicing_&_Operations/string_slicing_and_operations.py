sentence = "Python is a powerful language."

# String Slicing:
word_1 = sentence[0:6]
word_2 = sentence[12:20]
word_3 = sentence[21:-1]
reversed_sentence = sentence[::-1]
new_sentence = (word_1 + " is a " + word_2 + " tool.") # Concatenatio


# Print Results:
print(f"Original sentence: {sentence}")
print("-" * 30) # A separator for clarity

print(f"Extracted word 1 (positive slicing): {word_1}")
print(f"Extracted word 2 (positive slicing): {word_2}")
print(f"Extracted word 3 (negative slicing): {word_3}")
print(f"Reversed sentence: {reversed_sentence}")
print(f"The length of the sentence is: {len(sentence)}") # Length
print(f"Concatenated sentence: {new_sentence}") # Concatination
print(f"Word 1 repeated 3 times: {word_1 * 3}") # Repetation