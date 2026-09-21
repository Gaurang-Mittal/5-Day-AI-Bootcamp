# Create a string
text = "Hello World Python"

# Reverse the entire string
reverse_string = text[::-1]

print("Original string:", text)
print("Reversed string:", reverse_string)

# Reverse the order of words
reverse_words = " ".join(text.split()[::-1])

print("Reversed words:", reverse_words)