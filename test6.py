import random

# Define the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Randomly choose an answer
answer = random.choice(alphabet)
print(f"Answer: {answer}")  # This is for debugging purposes. Remove or comment out in the actual game.

# Initialize the counter and histogram
counter = 0
histogram = [0, 0, 0, 0, 0, 0, 0]  # a-d, e-h, ..., y-z

# Game loop
while True:
    counter += 1
    guess = input("Guess the lowercase alphabet: ")

    if guess < "a" or guess > "z":
        print("Please enter a lowercase alphabet.")
        continue

    diff = (ord(guess) - ord("a")) // 4  # Calculate corresponding pair index
    histogram[diff] += 1

    if guess == answer:
        print(f"Congratulations! You guessed the alphabet {answer} in {counter} tries")
        break
    elif guess < answer:
        print("The alphabet you are looking for is alphabetically higher.")
    else:
        print("The alphabet you are looking for is alphabetically lower.")

# Display the histogram
print("Guess Histogram:")
print(histogram)
print(f"a - d: {'*' * histogram[0]}")
print(f"e - h: {'*' * histogram[1]}")
print(f"i - l: {'*' * histogram[2]}")
print(f"m - p: {'*' * histogram[3]}")
print(f"q - t: {'*' * histogram[4]}")
print(f"u - x: {'*' * histogram[5]}")
print(f"y - z: {'*' * histogram[6]}")
