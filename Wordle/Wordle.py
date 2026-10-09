import random

with open("Wordle/words.txt") as f:
    words = f.read().splitlines()

with open("Wordle/guesses.txt") as f:
    guesses = f.read().splitlines()

green = "\033[32m"
yellow = "\033[33m"
gray = "\033[90m"
reset = "\033[0m"

word = random.choice(words)

guessesleft = 6

print(f"{green}\n==== WORDLE ====\n{reset}")

while True:

    print("Guesses remaining:", guessesleft)

    guess = input("Enter your guess: ").lower()

    if len(guess) != 5:
        print("Guess must be 5 letters long.")
        continue

    elif guess not in guesses and guess not in words:
        print("Not in word list.")
        continue

    guessesleft -= 1
    colors = [None] * 5
    temp = word

    for i, c in enumerate(guess):
            if temp[i] == c:
                colors[i] = green
                temp = temp[:i] + "_" + temp[i+1:]

    for i, c in enumerate(guess):
        if colors[i] is None:
            if c in temp:
                colors[i] = yellow
                temp = temp[:temp.find(c)] + "_" + temp[temp.find(c)+1:]
            else:
                colors[i] = gray

    result = "".join(
        f"{colors[i]}{c}{reset}" 
        for i, c in enumerate(guess))
    
    print(result)

    if guess == word:
        print(f"{green}Congratulations! You guessed the word!{reset}")
        break

    elif guessesleft == 0:
        print(f"Out of guesses! The word was: {green}{word}{reset}")
        break
