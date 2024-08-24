def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

# Example usage:
input_string = "myname"
reversed_string = reverse_words(input_string)
print(reversed_string)