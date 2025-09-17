# Create a function that returns a list of cubes for odd numbers in a given range

def cubes_of_odds(start, end):
    return [x**3 for x in range(start, end + 1) if x % 2 != 0]

print(cubes_of_odds(1, 10))

# Create a function that creates a list of uppercase words longer than 3 characters
def long_upper_words(words):
    return [word.upper() for word in words if len(word) > 3]

words = {"Polytechnic", "COP", "oop", "StUdEnT"}
print(long_upper_words(words))

# Return a dictionary mapping each word to its length
def word_lengths(words):
    return {word: len(word) for word in words}

print(word_lengths(words))