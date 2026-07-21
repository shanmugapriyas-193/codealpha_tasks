import random

words = ["apple", "banana", "cat", "dog", "book"]
word = random.choice(words)

guessed = ""
attempts = 6

print("Guess the word letter by letter")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter a letter: ")
    guessed += guess

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over. Word was:", word)