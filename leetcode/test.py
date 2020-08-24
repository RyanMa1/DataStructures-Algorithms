import random

# prints hangman and chooses a random word from the word bank
print("H A N G M A N")
word_bank = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_bank)

# the code below is from when i had to show the first 3 letters and the make the rest "-"
# var1 = guess_word[:3]
# var2 = guess_word[3:]
# var3 = int(len(var2))
# guess = input("Guess the word {0}{1}: ".format(var1, "-" * var3))

# this keeps record of what letters where attempted and what attempt we are on
attempt_list = []
attempts = 0

# this is the actual game loop that asks for the letter
while attempts != 8:
    print("")
    for char in guess_word:
        if char in attempt_list and guess_word:
            print(char, end="")
        else:
            print("-", end="")
    print("")
    guess = input("Input a letter: \n")
    if guess in attempt_list:
        attempts += 1
    elif guess not in guess_word:
        attempts += 1
        print("No such letter in the word")
    attempt_list.append(guess)

# print(attempt_list)
# print(attempts)

if guess == guess_word:
    print("You survived!")
else:
    print("""
Thanks for playing!
We'll see how well you did in the next stage""")